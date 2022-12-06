// Code generated by protoc-gen-go-copy. DO NOT EDIT.
// source: kentik/user/v202211/user.proto

package user

import "google.golang.org/protobuf/types/known/timestamppb"

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *PermissionEntry) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *PermissionEntry:
		x.Capability = v.GetCapability()
		x.Allowed = v.GetAllowed()
	default:
		if v, ok := v.(interface{ GetCapability() string }); ok {
			x.Capability = v.GetCapability()
		}
		if v, ok := v.(interface{ GetAllowed() bool }); ok {
			x.Allowed = v.GetAllowed()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *PermissionEntry) Proto_ShallowClone() (c *PermissionEntry) {
	if x != nil {
		c = new(PermissionEntry)
		c.Capability = x.Capability
		c.Allowed = x.Allowed
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *User) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *User:
		x.Id = v.GetId()
		x.UserEmail = v.GetUserEmail()
		x.UserFullName = v.GetUserFullName()
		x.Role = v.GetRole()
		x.Permissions = v.GetPermissions()
		x.Filter = v.GetFilter()
		x.LastLogin = v.GetLastLogin()
		x.Cdate = v.GetCdate()
		x.Edate = v.GetEdate()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
		if v, ok := v.(interface{ GetUserEmail() string }); ok {
			x.UserEmail = v.GetUserEmail()
		}
		if v, ok := v.(interface{ GetUserFullName() string }); ok {
			x.UserFullName = v.GetUserFullName()
		}
		if v, ok := v.(interface{ GetRole() Role }); ok {
			x.Role = v.GetRole()
		}
		if v, ok := v.(interface{ GetPermissions() []*PermissionEntry }); ok {
			x.Permissions = v.GetPermissions()
		}
		if v, ok := v.(interface{ GetFilter() string }); ok {
			x.Filter = v.GetFilter()
		}
		if v, ok := v.(interface{ GetLastLogin() *timestamppb.Timestamp }); ok {
			x.LastLogin = v.GetLastLogin()
		}
		if v, ok := v.(interface{ GetCdate() *timestamppb.Timestamp }); ok {
			x.Cdate = v.GetCdate()
		}
		if v, ok := v.(interface{ GetEdate() *timestamppb.Timestamp }); ok {
			x.Edate = v.GetEdate()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *User) Proto_ShallowClone() (c *User) {
	if x != nil {
		c = new(User)
		c.Id = x.Id
		c.UserEmail = x.UserEmail
		c.UserFullName = x.UserFullName
		c.Role = x.Role
		c.Permissions = x.Permissions
		c.Filter = x.Filter
		c.LastLogin = x.LastLogin
		c.Cdate = x.Cdate
		c.Edate = x.Edate
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ListUsersRequest) Proto_ShallowCopy(v interface{}) {
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ListUsersRequest) Proto_ShallowClone() (c *ListUsersRequest) {
	if x != nil {
		c = new(ListUsersRequest)
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ListUsersResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *ListUsersResponse:
		x.Users = v.GetUsers()
		x.InvalidCount = v.GetInvalidCount()
	default:
		if v, ok := v.(interface{ GetUsers() []*User }); ok {
			x.Users = v.GetUsers()
		}
		if v, ok := v.(interface{ GetInvalidCount() uint32 }); ok {
			x.InvalidCount = v.GetInvalidCount()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ListUsersResponse) Proto_ShallowClone() (c *ListUsersResponse) {
	if x != nil {
		c = new(ListUsersResponse)
		c.Users = x.Users
		c.InvalidCount = x.InvalidCount
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *GetUserRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *GetUserRequest:
		x.Id = v.GetId()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *GetUserRequest) Proto_ShallowClone() (c *GetUserRequest) {
	if x != nil {
		c = new(GetUserRequest)
		c.Id = x.Id
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *GetUserResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *GetUserResponse:
		x.User = v.GetUser()
	default:
		if v, ok := v.(interface{ GetUser() *User }); ok {
			x.User = v.GetUser()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *GetUserResponse) Proto_ShallowClone() (c *GetUserResponse) {
	if x != nil {
		c = new(GetUserResponse)
		c.User = x.User
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *CreateUserRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *CreateUserRequest:
		x.User = v.GetUser()
	default:
		if v, ok := v.(interface{ GetUser() *User }); ok {
			x.User = v.GetUser()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *CreateUserRequest) Proto_ShallowClone() (c *CreateUserRequest) {
	if x != nil {
		c = new(CreateUserRequest)
		c.User = x.User
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *CreateUserResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *CreateUserResponse:
		x.User = v.GetUser()
	default:
		if v, ok := v.(interface{ GetUser() *User }); ok {
			x.User = v.GetUser()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *CreateUserResponse) Proto_ShallowClone() (c *CreateUserResponse) {
	if x != nil {
		c = new(CreateUserResponse)
		c.User = x.User
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *UpdateUserRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *UpdateUserRequest:
		x.User = v.GetUser()
	default:
		if v, ok := v.(interface{ GetUser() *User }); ok {
			x.User = v.GetUser()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *UpdateUserRequest) Proto_ShallowClone() (c *UpdateUserRequest) {
	if x != nil {
		c = new(UpdateUserRequest)
		c.User = x.User
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *UpdateUserResponse) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *UpdateUserResponse:
		x.User = v.GetUser()
	default:
		if v, ok := v.(interface{ GetUser() *User }); ok {
			x.User = v.GetUser()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *UpdateUserResponse) Proto_ShallowClone() (c *UpdateUserResponse) {
	if x != nil {
		c = new(UpdateUserResponse)
		c.User = x.User
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *DeleteUserRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *DeleteUserRequest:
		x.Id = v.GetId()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *DeleteUserRequest) Proto_ShallowClone() (c *DeleteUserRequest) {
	if x != nil {
		c = new(DeleteUserRequest)
		c.Id = x.Id
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *DeleteUserResponse) Proto_ShallowCopy(v interface{}) {
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *DeleteUserResponse) Proto_ShallowClone() (c *DeleteUserResponse) {
	if x != nil {
		c = new(DeleteUserResponse)
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ResetApiTokenRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *ResetApiTokenRequest:
		x.Id = v.GetId()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ResetApiTokenRequest) Proto_ShallowClone() (c *ResetApiTokenRequest) {
	if x != nil {
		c = new(ResetApiTokenRequest)
		c.Id = x.Id
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ResetApiTokenResponse) Proto_ShallowCopy(v interface{}) {
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ResetApiTokenResponse) Proto_ShallowClone() (c *ResetApiTokenResponse) {
	if x != nil {
		c = new(ResetApiTokenResponse)
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ResetActiveSessionsRequest) Proto_ShallowCopy(v interface{}) {
	switch v := v.(type) {
	case *ResetActiveSessionsRequest:
		x.Id = v.GetId()
	default:
		if v, ok := v.(interface{ GetId() string }); ok {
			x.Id = v.GetId()
		}
	}
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ResetActiveSessionsRequest) Proto_ShallowClone() (c *ResetActiveSessionsRequest) {
	if x != nil {
		c = new(ResetActiveSessionsRequest)
		c.Id = x.Id
	}
	return
}

// Proto_ShallowCopy copies fields, from v to the receiver, using field getters.
// Note that v is of an arbitrary type, which may implement any number of the
// field getters, which are defined as any methods of the same signature as those
// generated for the receiver type, with a name starting with Get.
func (x *ResetActiveSessionsResponse) Proto_ShallowCopy(v interface{}) {
}

// Proto_ShallowClone returns a shallow copy of the receiver or nil if it's nil.
func (x *ResetActiveSessionsResponse) Proto_ShallowClone() (c *ResetActiveSessionsResponse) {
	if x != nil {
		c = new(ResetActiveSessionsResponse)
	}
	return
}