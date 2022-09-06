package app

import (
	"io"
	"moisture1/db"
	"moisture1/routes"
	"os"

	"github.com/gin-gonic/gin"
)

var app *gin.Engine

func start (){
	db.ConnectDB();
}

func CORSMiddleware() gin.HandlerFunc {
    return func(c *gin.Context) {
        c.Writer.Header().Set("Access-Control-Allow-Origin", "*")
        c.Writer.Header().Set("Access-Control-Allow-Credentials", "true")
        c.Writer.Header().Set("Access-Control-Allow-Headers", "Content-Type, Content-Length, Accept-Encoding, X-CSRF-Token, Authorization, accept, origin, Cache-Control, X-Requested-With")
        c.Writer.Header().Set("Access-Control-Allow-Methods", "POST, OPTIONS, GET, PUT")

        if c.Request.Method == "OPTIONS" {
            c.AbortWithStatus(204)
            return
        }

        c.Next()
    }
}

func init() {
	gin.DisableConsoleColor()

    // Logging to a file.
    f, _ := os.Create("gin.log")
    gin.DefaultWriter = io.MultiWriter(f)

	
	app = gin.Default()
	
	app.Use(CORSMiddleware())
	app.SetTrustedProxies([]string{"192.168.*.*"})
	
  	start()
  	routes.Register(app)
}

func Run(port string) {
	app.Run(port)
}