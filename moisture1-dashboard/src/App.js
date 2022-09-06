import React from "react";
import axios from "axios";
import { Card, Text, Badge, Group } from '@mantine/core';
import { useState } from 'react';
import {
  AppShell,
  Navbar,
  Header,
  MediaQuery,
  Burger,
  useMantineTheme,
} from '@mantine/core';

import {
  CartesianGrid,
  Cell,
  ResponsiveContainer,
  Scatter,
  ScatterChart,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';
import moment from 'moment';


const FIVE_MINUTES = 300*1000;

const plantAliases = {
  "C8:C9:A3:54:1B:6C":"Dieffenbachia"
}

const baseurl = "http://192.168.0.215:8000"
const allReadings = baseurl + "/api/readings"

function evaluateReading(reading) {
  if (reading > 80) {
    return ["Very Good", "green"]
  } else if (reading <=80 && reading >=50) {
    return ["Good", "yellow"]
  } else {
    return ["Poor", "red "]
  }
}

const TimeSeriesChart = ({ chartData, lastReadingColor }) => {
  return (
  <ResponsiveContainer width = '95%' height = {300} >
    <ScatterChart>
    <CartesianGrid strokeDasharray="1 1"/>
      <XAxis
        dataKey = 'CreatedAt'
        domain = {['auto', 'auto']}
        name = 'Time'
        tickFormatter = {(unixTime) => moment(unixTime).format('hh:mma ddd')}
      />
      <YAxis dataKey = 'reading' name = 'Reading' />
      <Tooltip/>
      <Scatter
        data = {chartData}
        line = {{ stroke: "#eee" }}
        lineJointType = 'monotoneX'
        lineType = 'joint'
        name = 'Readings'
      >
        {chartData.map((entry, index) => (
          <Cell key={`cell-${index}`} fill={evaluateReading(entry.reading)[1]} />
        ))}
      </Scatter>

    </ScatterChart>
  </ResponsiveContainer>
  )
}

function MonitorCard(props) {
  const { macAddress, readings } = props;

  const [lastReadingStatus, lastReadingColor] = evaluateReading(readings.at(-1).reading)

  return (
    <>
    
    <Card shadow="sm" p="lg" radius="md" withBorder>
    <br/>
      <Card.Section>
        <TimeSeriesChart chartData={readings.slice(-20)} lastReadingColor={lastReadingColor}/>
      </Card.Section>

      <Group position="apart" mt="md" mb="xs">
        <Text weight={500}>{plantAliases[macAddress]}</Text>
        <Badge color="pink" variant="light">
          {macAddress}
        </Badge>
      </Group>

      <Group position="apart" mt="md" mb="xs">
        <Text size="sm">
        Last Measurement: {readings.at(-1).reading}%  
      </Text>
        <Badge color={lastReadingColor} variant="light">
          {lastReadingStatus}
        </Badge>
      </Group>
    </Card>
    </>
  )
}

function MonitorDeck() {
  const [readings, setReadings] = React.useState({})
  const [lastUpdate, setLastUpdate] = React.useState(new Date('1970-01-01Z00:00:00:000'))

  

  const fetchReadings = () => {
    axios.get(allReadings)
      .then((res)=>{
        const readings_ = res.data.readings.reduce((readingsSoFar, { macAddress, CreatedAt, reading }) => {
          if (!readingsSoFar[macAddress]) readingsSoFar[macAddress] = [];
          readingsSoFar[macAddress].push({ macAddress, CreatedAt, reading });
          return readingsSoFar;
        }, {});
        setReadings(readings_)
      })
      .catch(err => {
        console.log(err);
      })
  }

  React.useEffect(()=> {
    fetchReadings();
    setLastUpdate(new Date());
    const interval = setInterval(() => {
      fetchReadings();
      setLastUpdate(new Date());
    }, FIVE_MINUTES);
    return () => clearInterval(interval);
  },[])

  return (
    <>
    <Group position="apart" mt="md" mb="xs">
        <Badge color="red" variant="light">
        Last Refresh: {moment(lastUpdate).format('LLLL')}
        </Badge>
      </Group>

    {
      Object.keys(readings).map((macAddress, index) =>
        <MonitorCard key={index} macAddress={macAddress} readings={readings[macAddress]} />
      )
    }
    </>
  )
}

function Shell() {
  const theme = useMantineTheme();
  const [opened, setOpened] = useState(false);
  return (
    <AppShell
      styles={{
        main: {
          background: theme.colorScheme === 'dark' ? theme.colors.dark[8] : theme.colors.gray[0],
        },
      }}
      navbarOffsetBreakpoint="sm"
      asideOffsetBreakpoint="sm"
      navbar={
        <Navbar p="md" hiddenBreakpoint="sm" hidden={!opened} width={{ sm: 75, lg: 150 }}>
          <Text>Dashboard</Text>
        </Navbar>
      }
      header={
        <Header height={70} p="md">
          <div style={{ display: 'flex', alignItems: 'center', height: '100%' }}>
            <MediaQuery largerThan="sm" styles={{ display: 'none' }}>
              <Burger
                opened={opened}
                onClick={() => setOpened((o) => !o)}
                size="sm"
                color={theme.colors.gray[6]}
                mr="xl"
              />
            </MediaQuery>

            <Text>Moisture1</Text>
          </div>
        </Header>
      }
    >
      <MonitorDeck/>
    </AppShell>
  );
}

function App() {
  return (
    <div className="App">
      <Shell/>
    </div>
  );
}

export default App;
