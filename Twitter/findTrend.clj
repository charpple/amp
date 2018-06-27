
(ns count-words
  (:require [clojure.string :as str]))

(defn get-word-counts [text]
  (reduce
    (fn [words word] (assoc words word (inc (words word 0))))
    {}

    (str/split (.toLowerCase text) #"\s+")))
(def cfreq 0)


(defn get-pretty-string [word-counts]
  (str/join "\n" (map (fn [[word freq]]
                         (str freq ": " word)
                      )
                      (sort-by val > word-counts))))

(time
  (let [in  "tweets.csv"
        out "output.txt"]
    (->> (slurp in)
      get-word-counts
      get-pretty-string
      (spit out)))
)
(println (re-find #"#.*" (slurp "output.txt")))

(spit "trend.txt" (re-find #"#.*" (slurp "output.txt")))

(spit "tweeter.txt" (re-find #"@\d+.*" (slurp "output.txt")))
