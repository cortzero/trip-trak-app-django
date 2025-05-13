from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView
from .models import Trip, Note

class HomeView(TemplateView):
  template_name = 'trip/index.html'

# --- Trip Views ---

class TripCreateView(CreateView):
  model = Trip
  success_url = reverse_lazy('trip-list')
  fields = ['city', 'country', 'start_date', 'end_date']
  # template named trip_form.html

  def form_valid(self, form):
    # Check if the owner field = logged in user
    form.instance.owner = self.request.user
    return super().form_valid(form)

class TripDetailView(DetailView):
  model = Trip
  # default template trip_detail.html

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    trip = context['object']
    notes = trip.notes.all()
    context['notes'] = notes
    return context
  
class TripUpdateView(UpdateView):
  model = Trip
  success_url = reverse_lazy('trip-list')
  fields = ['city', 'country', 'start_date', 'end_date']
  # template trip_form.html
  
class TripDeleteView(DeleteView):
  model =Trip
  success_url = reverse_lazy('trip-list')

def trips_list(request):
  trips = Trip.objects.filter(owner=request.user)
  context = {'trips': trips}
  return render(request, 'trip/trip_list.html', context)


# --- Notes views ---

class NoteDetailView(DetailView):
  model = Note

class NoteListView(ListView):
  model = Note
  # default template note_list.html
  
  def get_queryset(self):
    queryset = Note.objects.filter(trip__owner=self.request.user)
    return queryset

class NoteCreateView(CreateView):
  model = Note
  success_url = reverse_lazy('note-list')
  fields = "__all__"
  # template note_form.html

  def get_form(self):
    form = super(NoteCreateView, self).get_form()
    trips = Trip.objects.filter(owner=self.request.user)
    form.fields['trip'].queryset = trips
    return form

class NoteUpdateView(UpdateView):
  model = Note
  success_url = reverse_lazy('note-list')
  fields = "__all__"
  # template note_form.html uses the same template for creation

  def get_form(self):
    form = super(NoteUpdateView, self).get_form()
    trips = Trip.objects.filter(owner=self.request.user)
    form.fields['trip'].queryset = trips
    return form

class NoteDeleteView(DeleteView):
  model = Note
  success_url = reverse_lazy('note-list')
  # No template - send a Post request to this url
