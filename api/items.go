package main

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getItems(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var items []entities.Item
		db.Raw("SELECT * FROM Items").Scan(&items)

		context.JSON(http.StatusOK, items)
	}
}
