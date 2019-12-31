# Copyright 2002-2008 Wichert Akkerman. All rights reserved.
# Copyright 2007-2008 Simplon. All rights reserved.
#
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
# 3. Neither the name of the University nor the names of its contributors
# may be used to endorse or promote products derived from this software
# without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
# OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
# OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
# SUCH DAMAGE.
"""Python RADIUS client code.

pyrad is an implementation of a RADIUS client as described in RFC2865.
It takes care of all the details like building RADIUS packets, sending
them and decoding responses.

Here is an example of doing a authentication request::

  import pyrad.packet
  from pyrad.client import Client
  from pyrad.dictionary import Dictionary

  srv = Client(server="radius.my.domain", secret="s3cr3t",
    dict = Dictionary("dicts/dictionary", "dictionary.acc"))

  req = srv.CreatePacket(code=pyrad.packet.AccessRequest,
        User_Name = "wichert", NAS_Identifier="localhost")
  req["User-Password"] = req.PwCrypt("password")

  reply = srv.SendPacket(req)
  if reply.code = =pyrad.packet.AccessAccept:
      print "access accepted"
  else:
      print "access denied"

  print "Attributes returned by server:"
  for i in reply.keys():
      print "%s: %s" % (i, reply[i])


This package contains four modules:

  - client: RADIUS client code
  - dictionary: RADIUS attribute dictionary
  - packet: a RADIUS packet as send to/from servers
  - tools: utility functions
"""

__docformat__ = 'epytext en'

__author__ = 'Wichert Akkerman <wichert@wiggy.net>'
__url__ = 'http://www.wiggy.net/code/pyrad.xhtml'
__copyright__ = 'Copyright 2002-2007 Wichert Akkerman'

__all__ = ['client', 'dictionary', 'packet', 'server', 'tools', 'dictfile']
