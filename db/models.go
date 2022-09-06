package db

import "time"

type SensorReading struct {
	ID     uint   `gorm:"primary_key"`
	CreatedAt time.Time
	MACAddress string `json:"macAddress"`
	Reading uint `json:"reading"`
}