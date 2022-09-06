package routes

import (
	"moisture1/db"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

var lastSentEmail time.Time

func Register(app *gin.Engine){
	lastSentEmail = time.Time{}

	r := app.Group("/api")

	r.GET("/readings", getAll)
	r.GET("/reading/:mac", getMac)
	r.PUT("/reading", addReading)
}

func getAll(c *gin.Context) {
	var sensorReadings []db.SensorReading
	db.DB.Find(&sensorReadings)
	c.JSON(http.StatusOK, gin.H{"readings": sensorReadings})
}

func getMac(c *gin.Context) {
	var sensorReadings []db.SensorReading
	mac := c.Param("mac")
	db.DB.Where("mac_address = ?", mac).Find(&sensorReadings)

	c.JSON(http.StatusOK, gin.H{"mac": mac, "readings": sensorReadings})
}



func addReading(c *gin.Context) {
	var sensorReading db.SensorReading
	c.BindJSON(&sensorReading)
	result := db.DB.Create(&sensorReading)

	if result.Error != nil {
		c.JSON(http.StatusInternalServerError, result.Error)
	}

	if reading := sensorReading.Reading; reading <= 70 {
		dt := time.Now()

		if yesterday := dt.Add(-time.Hour * 24); lastSentEmail.Before(yesterday) {
			SendWaterWarning("Status: Please Water", "Hello! \n\nIt's me, your plant! Please water me!\nThank you :)")
			lastSentEmail=dt
		}
	}
	
	
	

	c.JSON(http.StatusOK, gin.H{"inserted": sensorReading.ID})
}