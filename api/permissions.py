from rest_framework.permissions import BasePermission



#for modifying the booking (later) -samira  [ICEBOX FEATURE]
# class IsBookingOwner(BasePermission):
# 	message = "You must be the owner of this booking"

# 	def has_object_permission(self, request, view, obj):
# 		if request.user.is_staff or (obj.user == request.user):
# 			return True
# 		else:
# 			return False