package server

import (
	"hash/fnv"
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

type PostUserRequest struct {
	Name     string `json:"name"`
	Email    string `json:"email"`
	Password string `json:"password"`
}

type PostUserResponse struct {
	ID    uint64 `json:"id"`
	Name  string `json:"name"`
	Email string `json:"email"`
}

func postUser(db *gorm.DB) gin.HandlerFunc {
	return func(context *gin.Context) {
		var request PostUserRequest
		context.Bind(&request)

		salt := getSalt()
		saltedPassword := request.Password + salt

		hasher := fnv.New128()
		hasher.Write([]byte(saltedPassword))

		result := db.Omit("ID").Create(&entities.User{
			Name:         request.Name,
			Email:        request.Email,
			PasswordHash: string(hasher.Sum([]byte{})),
			PasswordSalt: salt,
		})

		if result.Error == nil && result.RowsAffected == 1 {
			var createdUser entities.User
			db.Find(&createdUser, "email = ?", request.Email)

			context.JSON(http.StatusCreated, PostUserResponse{
				ID:    createdUser.ID,
				Name:  createdUser.Name,
				Email: createdUser.Email,
			})

			return
		}

		context.JSON(http.StatusBadRequest, []entities.User{})
	}
}
