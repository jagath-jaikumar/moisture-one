package routes

import (
	"crypto/tls"
	"fmt"
	"log"
	"os"

	gomail "gopkg.in/mail.v2"

	"github.com/joho/godotenv"
)


var emailPassword string
var emailAccount string
var recipientEmail string

func init() {
	err := godotenv.Load()
	if err != nil {
		log.Fatal("Error loading .env file")
	}
	
	emailPassword = os.Getenv("EMAIL_PASSWORD")
	emailAccount = os.Getenv("EMAIL_ACCOUNT")
  recipientEmail = os.Getenv("RECIPIENT_EMAIL")
}

func SendWaterWarning(header string, message string) {
  m := gomail.NewMessage()

  // Set E-Mail sender
  m.SetHeader("From", emailAccount)

  // Set E-Mail receivers
  m.SetHeader("To", recipientEmail)

  // Set E-Mail subject
  m.SetHeader("Subject", header)

  // Set E-Mail body. You can set plain text or html with text/html
  m.SetBody("text/plain", message)

  // Settings for SMTP server
  d := gomail.NewDialer("smtp.gmail.com", 587, emailAccount, emailPassword)

  // This is only needed when SSL/TLS certificate is not valid on server.
  // In production this should be set to false.
  d.TLSConfig = &tls.Config{InsecureSkipVerify: true}

  // Now send E-Mail
  if err := d.DialAndSend(m); err != nil {
    fmt.Println(err)
    panic(err)
  }

  return
}