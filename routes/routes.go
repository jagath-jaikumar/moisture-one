package routes

import (
	"moisture1/db"
	"net/http"

	"github.com/gin-gonic/gin"
)

func Register(app *gin.Engine){
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
	
	c.JSON(http.StatusOK, gin.H{"inserted": sensorReading.ID})
}