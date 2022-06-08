package main

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func GetUsers(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var users []User
		db.Raw("SELECT * FROM Users").Scan(&users)

		context.JSON(http.StatusOK, users)
	}
}

func PostUser(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var user User
		context.Bind(&user)

		result := db.Create(user)

		if result.Error == nil && result.RowsAffected == 1 {
			var users []User
			db.Raw("SELECT * FROM Users").Scan(&users)

			context.JSON(http.StatusCreated, users)
			return
		}

		context.JSON(http.StatusInternalServerError, []User{})
	}
}
