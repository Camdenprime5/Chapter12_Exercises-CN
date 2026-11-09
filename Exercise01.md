# Exercise 1 - Ask a Virtual Assistant

## Question 1: How does `setdefault()` work?

The `setdefault()` method checks whether a key already exists in a dictionary.

If the key exists, it returns the value already associated with that key. If the key does not exist, it adds the key using the default value provided and then returns that value.

For example:

```python
successor_map.setdefault("half", []).append("a")
```

If `"half"` is not already in the dictionary, Python creates the key with an empty list and then appends `"a"` to that list. If `"half"` already exists, Python uses the existing list and appends `"a"` to it.

## Question 2: Rewrite `add_bigram()` using `setdefault()`

The longer version could look like this:

```python
successor_map = {}

def add_bigram(bigram):
    first, second = bigram

    if first not in successor_map:
        successor_map[first] = [second]
    else:
        successor_map[first].append(second)
```

Using `setdefault()`, it can be shortened to:

```python
successor_map = {}

def add_bigram(bigram):
    first, second = bigram
    successor_map.setdefault(first, []).append(second)
```

I prefer the `setdefault()` version because it does the same job with less code while still being readable.

## Question 3: What are the differences between large language models like GPT and Markov chain text generation?

Markov chains and large language models can both generate text by using patterns found in existing text, but they work very differently.

A Markov chain looks at a small amount of previous text, such as one or two words, and uses recorded word combinations to decide what word can come next. For example, the Chapter 12 exercises use two previous words as a bigram and store possible third words in a successor map. The amount of context used by the model is therefore limited.

Large language models such as GPT use neural networks and can consider a much larger amount of context. Instead of storing exact word transitions in a dictionary, they learn statistical patterns in language during training. This allows them to recognize more complicated relationships between words and produce text that is generally more coherent.

Markov chains are much simpler and easier to build because they mostly involve counting and randomly selecting from previously observed combinations. Large language models require much more training data and computing power.

The main similarity is that both approaches use patterns from previous text to help determine what may come next. The main difference is that a Markov chain uses direct local transitions from its source text, while a large language model uses learned patterns and a much larger context.