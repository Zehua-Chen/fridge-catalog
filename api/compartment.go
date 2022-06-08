package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func GetCompartment(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var compartments []Compartment
		db.Raw("SELECT * FROM Compartments").Scan(&compartments)

		context.JSON(http.StatusOK, compartments)
	}
}

func PostCompartment(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var compartment Compartment
		context.Bind(&compartment)

		db.Create(compartment)
		context.String(http.StatusOK, "")
	}
}
