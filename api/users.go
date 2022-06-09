package main

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/models"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getUsers(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var users []models.User
		db.Raw("SELECT * FROM Users").Scan(&users)

		context.JSON(http.StatusOK, users)
	}
}

func postUser(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var user models.User
		context.Bind(&user)

		result := db.Create(user)

		if result.Error == nil && result.RowsAffected == 1 {
			var users []models.User
			db.Raw("SELECT * FROM Users").Scan(&users)

			context.JSON(http.StatusCreated, users)
			return
		}

		context.JSON(http.StatusInternalServerError, []models.User{})
	}
}
