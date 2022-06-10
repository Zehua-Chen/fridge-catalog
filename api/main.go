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

	apiV1.GET("/compartments", getCompartments(db))
	apiV1.POST("/compartments", postCompartment(db))

	apiV1.GET("/users", getUsers(db))
	apiV1.POST("/users", postUser(db))

	apiV1.GET("/markets", getMarkets(db))
	apiV1.POST("/markets", postMarkets(db))

	apiV1.GET("/nutrients", getNutrients(db))
	apiV1.POST("/nutrients", postNutrient(db))

	apiV1.GET("/methods", getMethods(db))
	apiV1.POST("/methods", postMethod(db))

	engine.Run("localhost:4000")
}
