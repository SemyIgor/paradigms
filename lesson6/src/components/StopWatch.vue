<template>
   <div>
      <h1>Секундомер</h1>
      <div class="stop-watch__screen">
         {{ hoursStr }}:{{ minutesStr }}:{{ secondsStr }}:<span>{{ msecondsStr }}</span>
      </div>

      <button @click="startTimer" class="btn">{{ startBtnText }}</button>
      <button @click="stopTimer" class="btn">RESET</button>
   </div>
</template>

<script>
export default {
   name: 'StopWatch',

   computed: {
      startBtnText() {
         return this.showStartSign ? 'START' : 'STOP';
      },
      hoursStr() {
         return this.hours.toString().padStart(2, '0');
      },
      minutesStr() {
         return this.minutes.toString().padStart(2, '0');
      },
      secondsStr() {
         return this.seconds.toString().padStart(2, '0');
      },
      msecondsStr() {
         return this.mseconds.toString().padStart(2, '0');
      },
   },

   data() {
      return {
         showStartSign: true,
         timerIsWorking: false,
         hours: 0,
         minutes: 0,
         seconds: 0,
         mseconds: 0,
         interval: null,
      };
   },
   methods: {
      updateTime() {
         this.mseconds++;
         if (this.mseconds === 10) {
            this.seconds++;
            this.mseconds = 0;
         }
         if (this.seconds === 60) {
            this.minutes++;
            this.seconds = 0;
         }
         if (this.minutes === 60) {
            this.hours++;
            this.minutes = 0;
         }
         if (this.hours === 24) {
            this.seconds = 0;
            this.minutes = 0;
            this.hours = 0;
         }
      },
      startTimer() {
         this.showStartSign = !this.showStartSign;
         this.timerIsWorking = true;
         if (!this.showStartSign) {
            this.interval = setInterval(this.updateTime, 100);
         } else {
            clearInterval(this.interval);
         }

      },
      stopTimer() {
         if (this.timerIsWorking) {
            this.hours = 0;
            this.minutes = 0;
            this.seconds = 0;
            this.mseconds = 0;
            clearInterval(this.interval);
            this.timerIsWorking = false;
            this.showStartSign = true;
         }
      }
   },

}
</script>

<style lang="scss" scoped>
span {
   font-size: 18px;
}

.btn {
   padding: 10px 20px;
   margin-top: 30px;
   margin: 30px 10px;
   cursor: pointer;
   border-radius: 50% 50%;
}

.stop-watch__screen {
   font-size: 24px;
   background-color: limegreen;
   color: white;
   padding-top: 10px;
   padding-bottom: 10px;
   margin: 0 auto;
   max-width: 200px;
   border-radius: 5px;
}
</style>