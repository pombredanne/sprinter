FAQ
===

Sprinter keeps injecting itself after my configuration! How do I override it?
-----------------------------------------------------------------------------

Sprinter will always inject itself after everything in a profile or rc
file, with the exception of text in a block surrounded by
#SPRINTER_OVERRIDES. These will always run after any sprinter
configuration.