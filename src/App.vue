<template>
  <v-app>
    <v-toolbar app style="z-index:1">
      <v-toolbar-side-icon></v-toolbar-side-icon>
      <v-toolbar-title ></v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items class="hidden-sm-and-down">
      <v-btn flat>Account</v-btn>
    </v-toolbar-items> 
    </v-toolbar>

    <v-content>
          <v-navigation-drawer style="position: absolute;z-index:0">
  <v-list two-line>
    <template>
    <v-list-tile avatar>
      <v-list-tile-content>
  <v-list-tile-title>vdv</v-list-tile-title>
 <v-list-tile-title>vdvd</v-list-tile-title>
      </v-list-tile-content>
    </v-list-tile>
    </template>
  </v-list>
</v-navigation-drawer>
      <v-sheet height="400" width="800" style="margin:auto; position: relative">
        <!-- now is normally calculated by itself, but to keep the calendar in this date range to view events -->
        <v-calendar
          ref="calendar"
          :now="today"
          :value="today"
          color="primary"
          type="week"
        >
          <!-- the events at the top (all-day) -->
          <template v-slot:dayHeader="{ date }">
            <template v-for="event in eventsMap[date]">
              <!-- all day events don't have time -->
              <div
                v-if="!event.time"
                :key="event.title"
                class="my-event"
                @click="open(event)"
                v-html="event.title"
              ></div>
            </template>
          </template>
          <!-- the events at the bottom (timed) -->
          <template v-slot:dayBody="{ date, timeToY, minutesToPixels }">
            <template v-for="event in eventsMap[date]">
              <!-- timed events -->
              <div
                v-if="event.time"
                :key="event.title"
                :style="{ top: timeToY(event.time) + 'px', height: minutesToPixels(event.duration) + 'px' }"
                class="my-event with-time"
                @click="open(event)"
                v-html="event.title"
              ></div>
            </template>
          </template>
        </v-calendar>
      </v-sheet>
    </v-content>
  </v-app>
</template>

<script>


export default {
  name: 'App',
  components: {

  },
  data () {
    return {
       today: '2019-01-08',
      events: [
        {
          title: 'Weekly Meeting',
          date: '2019-01-07',
          time: '09:00',
          duration: 45
        },
        {
          title: 'Thomas\' Birthday',
          date: '2019-01-10'
        },
        {
          title: 'Mash Potatoes',
          date: '2019-01-09',
          time: '12:30',
          duration: 180
        }
      ]
    }
  },
  computed: {
      // convert the list of events into a map of lists keyed by date
      eventsMap () {
        const map = {}
        this.events.forEach(e => (map[e.date] = map[e.date] || []).push(e))
        return map
      }
    },
    mounted () {
      this.$refs.calendar.scrollToTime('08:00')
    },
    methods: {
      open (event) {
        alert(event.title)
      }
    }
}
</script>
<style lang="stylus" scoped>
  .my-event {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    border-radius: 2px;
    background-color: #1867c0;
    color: #ffffff;
    border: 1px solid #1867c0;
    font-size: 12px;
    padding: 3px;
    cursor: pointer;
    margin-bottom: 1px;
    left: 4px;
    margin-right: 8px;
    position: relative;

    &.with-time {
      position: absolute;
      right: 4px;
      margin-right: 0px;
    }
  }
</style>
