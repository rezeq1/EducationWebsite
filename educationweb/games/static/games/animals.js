
let baseCards = ['tree', 'horse', 'bird', 'tiger','panda','pelican','penguin','walrus'];

let possibleCards = baseCards.concat(baseCards); 
const numCards = possibleCards.length;
const maxMatch = baseCards.length; 
let opened = [];
let numStars = 3;
let numMatch = 0;
let numMoves = 0;



let seconds = 0;
let minutes = 0;
let t;


const showStar = ['<li><i class="fa fa-star"></i></li><li><i class="fa fa-star-o"></i></li><li><i class="fa fa-star-o"></i></li>',  // 1 star
                  '<li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star-o"></i></li>',  // 2 stars
                  '<li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li><li><i class="fa fa-star"></i></li>' // 3 stars
                 ];




function shuffle(array) {
    var currentIndex = array.length, temporaryValue, randomIndex;

    while (currentIndex !== 0) {
        randomIndex = Math.floor(Math.random() * currentIndex);
        currentIndex -= 1;
        temporaryValue = array[currentIndex];
        array[currentIndex] = array[randomIndex];
        array[randomIndex] = temporaryValue;
    }

    return array;
}



function initGame() {
   document.querySelector('.overlay').style.display = 'none';
   document.querySelector('.deck').innerHTML = '';
   shuffle(possibleCards);
   opened = [];
   numStars = 3;
   numMoves = 0;
   numMatch = 0;
   resetTimer();
   runTimer();
   printStars();
   printMoves();


   for(i=0;i<numCards;i++) {
        document.querySelector('.deck').innerHTML += `<li class="card"><img src="/media/games/${possibleCards[i]}.svg"/></li>`;
   };




  document.querySelectorAll(".card").forEach((card) => {
    card.addEventListener("click", function () {

    if (card.classList.contains('show')){
      return; 
    }

    card.classList.add('show','animated','flipInY');

    let currentCard = card.innerHTML;
    opened.push(currentCard);


    if(opened.length > 1) {
      if(currentCard === opened[0]) {
        match();
      }else {
        unmatch();
      }
    };
    
    starCount(); 
    printMoves();


    if(numMatch === maxMatch ) {
      stopTimer();
      congrats();
    }

    })
  });

};


initGame();


function match() {
  numMoves++;
  numMatch++;
  opened = [];

  document.querySelectorAll(".show").forEach((matchedCard) => {
    matchedCard.classList.add('match','animated','flip')
    matchedCard.classList.remove('show')
  });

};



function unmatch() {
  numMoves++;
  opened = [];

  document.querySelectorAll(".show:not(.match)").forEach((unmatchedCard) => {
    unmatchedCard.classList = 'card show unmatch animated shake';
    document.querySelectorAll('.unmatch').forEach((unmatchedCard) => {
      setTimeout(function() {
        unmatchedCard.classList = 'animated flipInY card';
      }, 600);
    })
  });
};



function starCount() {

  if(numMoves < 16) {
      numStars = 3;
    }else if (numMoves >= 16 && numMoves < 25) {
      numStars = 2;
    }else {
      numStars = 1;
    };

    printStars();
};


function printStars() {
  document.querySelectorAll('.stars').forEach(panel => panel.innerHTML = showStar[numStars-1])
}


function printMoves(){
  document.querySelectorAll('.moves').forEach(move => move.textContent = numMoves)
}




function twoDigits(number) {
       return (number < 10 ? '0' : '') + number;
}


function timer() {
    seconds++;
    if (seconds >= 60) {
        seconds = 0;
        minutes++;
    }
  
    updateTimer()
    runTimer();
}


function runTimer() {
  t = setTimeout(timer, 1000);
}

function resetTimer() {
    stopTimer();
    seconds = 0; minutes = 0;
    updateTimer()
}

function updateTimer(){
    document.querySelectorAll(".timer-seconds").forEach(item=> item.textContent = twoDigits(seconds));
    document.querySelectorAll(".timer-minutes").forEach(item=> item.textContent = twoDigits(minutes));
}

function stopTimer() {
  clearTimeout(t);
}



document.querySelectorAll('.restart').forEach(item=>
  item.addEventListener("click", function(){
    initGame();
  })
);



const finishImg = ['walrus', 'penguin','tiger'];
const finishMsg = ['Oh man... even a walrus can do better','Good job, pal! Well done','Geez, That\'s amazing!'];


function congrats() {
  stopTimer();
  setTimeout(function(){
      
      document.querySelector('.switch-msg').innerHTML = 
      `
        <h2>${finishMsg[numStars-1]}</h2>
        <img src="/media/games/${finishImg[numStars-1]}.svg" alt="" width="300">
      `
      document.querySelector('.overlay-content').classList.add('animated','bounceIn')
  }, 100);

  setTimeout(function(){
     document.querySelector('.overlay').style.display = 'block'
  }, 300);

};


document.querySelectorAll('.hint').forEach(item=>
  item.addEventListener("click", function(){
    setTimeout(function(){
      numMoves++;
      opened = [];
    
      document.querySelectorAll(".show:not(.match)").forEach((unmatchedCard) => {
        unmatchedCard.classList = 'card show unmatch animated shake';
        document.querySelectorAll('.unmatch').forEach((unmatchedCard) => {
          setTimeout(function() {
            unmatchedCard.classList = 'animated flipInY card';
          }, 600);
        })
      });
    }, 1500);
    
    document.querySelectorAll(".card").forEach((card) => {
      if (card.classList.contains('show')){
        return; 
      }
    
      card.classList.add('show','animated','flipInY');
    
      let currentCard = card.innerHTML;
      opened.push(currentCard);
    
    });
  })
);
