Release package - All PR's should be against staging/src/rocky-release

## Notes for Packagers/Builders

This package can produce multiple variants of `rocky-release`:

* Stable: `rocky-release`, `rocky-repos`, `rocky-gpg-keys`, etc
* LookAhead: All packages appended with `-lookahead`
* Beta: All packages appended with `-beta`

* If `--with=rllookahead` or `--with=rlbeta` are set in mock, those variants are built
* If both are set the same time, build will fail

When `--with=rllookahead` is set the minor version will typically be `y+1`. So if the current
stable is `X.0`, the next would be `X.1`.

For pre-releases/beta, both packages should produce `X.Y` until changed in the spec.

The `rllh` macro may be versioned out for future use. It does not have to be explicitly set.

A `rllh_minor` macro may be introduced in the future.

### How does this benefit us?

It provides an opportunity to do self testing of various kinds. In most cases,
a rocky-release package for the upcoming minor release will be built normally
and doesn't require the variant release packages. However, the option is at
least available for those who want to test something in particular and override
the default rocky-release packages.

### What is the rloverride macro?

This simply sets the dist tag to `.el%{major}.override` and changes the ID="..."
tag in `/etc/os-release` to read as `rhel` rather than `rocky`. This helps us
perform very specific builds that cannot otherwise be debranded properly, eg
dotnet. This should also change the initial macros to only provide `%rhel` and
not CentOS or any other derivative macro name, as some packages specifically
look for these macros being set as well and *also* applies to those packages
that cannot be properly debranded or when debranding has not visual or
functional benefit.
