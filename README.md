# skyjo

### Definitions:
* X: Value of card
* A: accept the ith card into your grid
* f: frequency of card

#### Simplified case:
* Consider the case where a card is taken from the stack and is accepted into the grid based on whether it is above or below a threshold.
* If it is above the threshold, the card is discarded back into the pile and shuffled.
* If it is below the threshold, the card is accepted arbitrarily into the grid.

![equation](http://www.sciweavers.org/tex2img.php?eq=E%28X%29%20%3D%20P%28A_1%29E%28X_1%29%20%2B%20P%28A_2%29E%28X_2%29%5C%5C%0AE%28X%29%20%3D%20%5Cfrac%7B%5Csum_%7B-2%7D%5E%7BT%7Df_%7Bi%7D%7D%7B150%7D%5Cfrac%7B%5Csum_%7B-2%7D%5E%7BT%7Dif_%7Bi%7D%7D%7B%5Csum_%7B-2%7D%5E%7BT%7Df_%7Bi%7D%7D%20%2B%20%5Cfrac%7B%5Csum_%7BT%7D%5E%7B12%7Df_%7Bi%7D%7D%7B150%7D%5Cfrac%7B%5Csum_%7B-2%7D%5E%7B12%7Dif_%7Bi%7D%7D%7B%5Csum_%7B-2%7D%5E%7B12%7Df_%7Bi%7D%7D%0A&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

<!-- E(X) = P(A_1)E(X_1) + P(A_2)E(X_2)\\ -->
<!-- // E(X) = \frac{\sum_{-2}^{T}f_{i}}{150}\frac{\sum_{-2}^{T}if_{i}}{\sum_{-2}^{T}f_{i}} + \frac{\sum_{T}^{12}f_{i}}{150}\frac{\sum_{-2}^{12}if_{i}}{\sum_{-2}^{12}f_{i}} -->
