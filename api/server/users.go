package server

import (
	"net/http"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/gin-gonic/gin"
	"gorm.io/gorm"
)

func getUsers(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var users []entities.User
		db.Find(&users)

		context.JSON(http.StatusOK, users)
	}
}

func postUser(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var user entities.User
		context.Bind(&user)

		result := db.Omit("ID").Create(&user)

		if result.Error == nil && result.RowsAffected == 1 {
			var returnUser entities.User
			db.Find(&returnUser, "email = ?", user.Email)

			context.JSON(http.StatusCreated, returnUser)
			return
		}

		context.JSON(http.StatusInternalServerError, []entities.User{})
	}
}
