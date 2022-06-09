package main

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getNutrients(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var nutrients []entities.Nutrient
		db.Raw("SELECT * FROM Nutrients").Scan(&nutrients)

		context.JSON(http.StatusOK, nutrients)
	}
}

func postNutrient(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var nutrient entities.Nutrient
		context.Bind(&nutrient)

		db.Create(&nutrient)

		context.String(http.StatusCreated, "")
	}
}
