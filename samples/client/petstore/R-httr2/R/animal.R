#' Create a new Animal
#'
#' @description
#' Animal Class
#'
#' @docType class
#' @title Animal
#' @description Animal Class
#' @format An \code{R6Class} generator object
#' @field className  character
#' @field color  character [optional]
#' @importFrom R6 R6Class
#' @importFrom jsonlite fromJSON toJSON
#' @export
Animal <- R6::R6Class(
  "Animal",
  public = list(
    `className` = NULL,
    `color` = NULL,
    #' Initialize a new Animal class.
    #'
    #' @description
    #' Initialize a new Animal class.
    #'
    #' @param className className
    #' @param color color. Default to "red".
    #' @param ... Other optional arguments.
    #' @export
    initialize = function(
        `className`, `color` = "red", ...
    ) {
      if (!missing(`className`)) {
        stopifnot(is.character(`className`), length(`className`) == 1)
        self$`className` <- `className`
      }
      if (!is.null(`color`)) {
        stopifnot(is.character(`color`), length(`color`) == 1)
        self$`color` <- `color`
      }
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return Animal in JSON format
    #' @export
    toJSON = function() {
      AnimalObject <- list()
      if (!is.null(self$`className`)) {
        AnimalObject[["className"]] <-
          self$`className`
      }
      if (!is.null(self$`color`)) {
        AnimalObject[["color"]] <-
          self$`color`
      }
      AnimalObject
    },
    #' Deserialize JSON string into an instance of Animal
    #'
    #' @description
    #' Deserialize JSON string into an instance of Animal
    #'
    #' @param input_json the JSON input
    #' @return the instance of Animal
    #' @export
    fromJSON = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      if (!is.null(this_object$`className`)) {
        self$`className` <- this_object$`className`
      }
      if (!is.null(this_object$`color`)) {
        self$`color` <- this_object$`color`
      }
      self
    },
    #' To JSON string
    #'
    #' @description
    #' To JSON String
    #'
    #' @return Animal in JSON format
    #' @export
    toJSONString = function() {
      jsoncontent <- c(
        if (!is.null(self$`className`)) {
          sprintf(
          '"className":
            "%s"
                    ',
          self$`className`
          )
        },
        if (!is.null(self$`color`)) {
          sprintf(
          '"color":
            "%s"
                    ',
          self$`color`
          )
        }
      )
      jsoncontent <- paste(jsoncontent, collapse = ",")
      json_string <- as.character(jsonlite::minify(paste("{", jsoncontent, "}", sep = "")))
    },
    #' Deserialize JSON string into an instance of Animal
    #'
    #' @description
    #' Deserialize JSON string into an instance of Animal
    #'
    #' @param input_json the JSON input
    #' @return the instance of Animal
    #' @export
    fromJSONString = function(input_json) {
      this_object <- jsonlite::fromJSON(input_json)
      self$`className` <- this_object$`className`
      self$`color` <- this_object$`color`
      self
    },
    #' Validate JSON input with respect to Animal
    #'
    #' @description
    #' Validate JSON input with respect to Animal and throw an exception if invalid
    #'
    #' @param input the JSON input
    #' @export
    validateJSON = function(input) {
      input_json <- jsonlite::fromJSON(input)
      # check the required field `className`
      if (!is.null(input_json$`className`)) {
        stopifnot(is.character(input_json$`className`), length(input_json$`className`) == 1)
      } else {
        stop(paste("The JSON input `", input, "` is invalid for Animal: the required field `className` is missing."))
      }
    },
    #' To string (JSON format)
    #'
    #' @description
    #' To string (JSON format)
    #'
    #' @return String representation of Animal
    #' @export
    toString = function() {
      self$toJSONString()
    },
    #' Return true if the values in all fields are valid.
    #'
    #' @description
    #' Return true if the values in all fields are valid.
    #'
    #' @return true if the values in all fields are valid.
    #' @export
    isValid = function() {
      # check if the required `className` is null
      if (is.null(self$`className`)) {
        return(FALSE)
      }

      TRUE
    },
    #' Return a list of invalid fields (if any).
    #'
    #' @description
    #' Return a list of invalid fields (if any).
    #'
    #' @return A list of invalid fields (if any).
    #' @export
    getInvalidFields = function() {
      invalid_fields <- list()
      # check if the required `className` is null
      if (is.null(self$`className`)) {
        invalid_fields["className"] <- "Non-nullable required field `className` cannot be null."
      }

      invalid_fields
    },
    #' Print the object
    #'
    #' @description
    #' Print the object
    #'
    #' @export
    print = function() {
      print(jsonlite::prettify(self$toJSONString()))
      invisible(self)
    }),
    # Lock the class to prevent modifications to the method or field
    lock_class = TRUE
)
## Uncomment below to unlock the class to allow modifications of the method or field
#Animal$unlock()
#
## Below is an example to define the print fnuction
#Animal$set("public", "print", function(...) {
#  print(jsonlite::prettify(self$toJSONString()))
#  invisible(self)
#})
## Uncomment below to lock the class to prevent modifications to the method or field
#Animal$lock()

