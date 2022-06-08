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

	}
}
