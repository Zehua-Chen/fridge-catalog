package main

import (
	"fmt"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func GetCompartment(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var compartment Compartment
		rows, _ := db.Raw("SELECT * FROM Compartments").Rows()

		defer rows.Close()

		for rows.Next() {
			db.ScanRows(rows, &compartment)
			fmt.Printf("level = %d, temperature = %f\n", compartment.Level, compartment.Temperature)
		}
	}
}
