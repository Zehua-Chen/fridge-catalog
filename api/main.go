package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func main() {
	db, err := gorm.Open(sqlite.Open("database.sqlite"), &gorm.Config{})

	if err != nil {
		fmt.Println(err.Error())
		return
	} else {
		fmt.Println(db.Name())
	}

	engine := gin.Default()
	apiV1 := engine.Group("/api/v1")

	apiV1.GET("/compartments", GetCompartment(db))

	engine.Run()
}
