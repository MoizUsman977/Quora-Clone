
class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    fields = ['name', 'email', 'username', 'age', 'gender', 'profile_picture']
    template_name = 'edit-user-data.html'
    success_url = reverse_lazy('profile') 
    
    def get_object(self, queryset=None):
        return self.request.user
