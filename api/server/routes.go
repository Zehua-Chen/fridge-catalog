package server

import (
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func SetupRouter(db *gorm.DB) *gin.Engine {
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

	apiV1.GET("/items", getItems(db))
	apiV1.PUT("/items", putItem(db))

	return engine
}
