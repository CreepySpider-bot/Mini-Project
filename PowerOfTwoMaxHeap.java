public class PowerOfTwoMaxHeap {
    private int[] data;
    private int x;
    private int size;
    public PowerOfTwoMaxHeap(int x) {
        this.x = x;
        this.data = new int[1];
        this.size = 0;
    }
    public void insert(int value) {
        // Check if the array needs to be resized
        if (size == data.length) {
            resizeArray();
        }
        // Add the new element to the end of the array
        data[size] = value;
        // Compare the new element to its parent and swap until it satisfies the heap property
        int currentIndex = size;
        while (currentIndex > 0 && data[currentIndex] > data[(currentIndex - 1) / (int) Math.pow(2, x)]) {
            int temp = data[currentIndex];
            data[currentIndex] = data[(currentIndex - 1) / (int) Math.pow(2, x)];
            data[(currentIndex - 1) / (int) Math.pow(2, x)] = temp;
            currentIndex = (currentIndex - 1) / (int) Math.pow(2, x);
        }
        size++;
    }
    public int popMax() {
        // Save the value of the root element
        int max = data[0];
        // Replace the root element with the last element in the array
        data[0] = data[size - 1];
        size--;
        // Compare the new root element to its children and swap until it satisfies the heap property
        int currentIndex = 0;
        while (currentIndex < size) {
            int maxChildIndex = currentIndex;
            // Find the largest child
            for (int i = 1; i <= (int) Math.pow(2, x); i++) {
                int childIndex = (int) Math.pow(2, x) * currentIndex + i;
                if (childIndex < size && data[childIndex] > data[maxChildIndex]) {
                    maxChildIndex = childIndex;
                }
            }
            // If the root element is smaller than the largest child, swap them
            if (data[currentIndex] < data[maxChildIndex]) {
                int temp = data[currentIndex];
                data[currentIndex] = data[maxChildIndex];
                data[maxChildIndex] = temp;
                currentIndex = maxChildIndex;
            } else {
                break;
            }
        }
        // Return the value of the original root element
        return max;
    }
    private void resizeArray() {
        int[] newData = new int[data.length * 2];
        for (int i = 0; i < data.length; i++) {
            newData[i] = data[i];
        }
        data = newData;
 
    }
 
 }
 
 