package main

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getCompartments(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var compartments []entities.Compartment
		db.Raw("SELECT * FROM Compartments").Scan(&compartments)

		context.JSON(http.StatusOK, compartments)
	}
}

func postCompartment(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var compartment entities.Compartment
		context.Bind(&compartment)

		db.Create(compartment)
		context.String(http.StatusOK, "")
	}
}
