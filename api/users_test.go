package main

import (
	"encoding/json"
	"io/ioutil"
	"net/http"
	"net/http/httptest"
	"testing"

	"github.com/Zehua-Chen/fridge-catalog/api/entities"
	"github.com/go-playground/assert/v2"
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func testPost(url string) {

}

func TestCreateUser(t *testing.T) {
	db, _ := gorm.Open(sqlite.Open("file::memory:?cache=shared"), &gorm.Config{})
	router := setupRouter(db)

	request, _ := http.NewRequest("POST", "/users", nil)

	response := httptest.NewRecorder()
	router.ServeHTTP(response, request)

	bytes, _ := ioutil.ReadAll(response.Body)

	var users []entities.User

	json.Unmarshal(bytes, &users)

	assert.Equal(t, 0, len(users))
}

func TestGetUsers2(t *testing.T) {
	// t.Fail()
}
