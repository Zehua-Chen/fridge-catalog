package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getMarkets(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var markets []Market
		db.Raw("SELECT * FROM Markets").Scan(&markets)

		context.JSON(http.StatusOK, markets)
	}
}
