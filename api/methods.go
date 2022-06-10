package main

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getMethods(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var methods []entities.PreparationMethod
		db.Raw("SELECT * FROM Preparation_Methods").Scan(&methods)

		context.JSON(http.StatusOK, methods)
	}
}

func postMethod(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var method entities.PreparationMethod
		context.Bind(&method)

		db.Create(&method)

		context.String(http.StatusCreated, "")
	}
}
