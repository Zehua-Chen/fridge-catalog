package main

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/models"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getMarkets(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var markets []models.Market
		db.Raw("SELECT * FROM Markets").Scan(&markets)

		context.JSON(http.StatusOK, markets)
	}
}

func postMarkets(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var market models.Market
		context.Bind(&market)

		db.Create(&market)

		context.String(http.StatusCreated, "")
	}
}
