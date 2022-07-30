package entities

type User struct {
	ID    uint64 `json:"id" gorm:"primaryKey;autoIncrement"`
	Email string `json:"email" gorm:"unique"`
	Name  string `json:"name"`
}
