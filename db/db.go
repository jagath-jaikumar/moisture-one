package db

import (
	"log"
	"os"

	"github.com/joho/godotenv"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)


type dbConnInfo struct {
	pg_host string
	pg_port string
	pg_name string
	pg_user string
	pg_pass string
	ssl_mode string
	
}

var dbInfo dbConnInfo
var DB *gorm.DB
var models = []interface{}{&SensorReading{}}



func init() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	
	dbInfo = dbConnInfo{
		pg_host: os.Getenv("PG_HOST"),
		pg_port: os.Getenv("PG_PORT"),
		pg_name: os.Getenv("PG_NAME"),
		pg_user: os.Getenv("PG_USER"),
		pg_pass: os.Getenv("PG_PASS"),
	}
}

func ConnectDB() {
	// dsn := fmt.Sprintf("host=%s user=%s password=%s dbname=%s sslmode=disable", dbInfo.pg_host, dbInfo.pg_user, dbInfo.pg_pass, dbInfo.pg_name)
	// db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
	
	db, err := gorm.Open(sqlite.Open("readings.db"), &gorm.Config{})

	if err != nil {
		log.Fatal("Could not connect to database")
	}

	db.AutoMigrate(models...)

	DB = db
}