#JCU RIF-CS Pre-Processor
#Copyright (C) 2012  Nigel Bajema, James Cook University
#
#This program is free software; you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation; either version 2 of the License, or
#(at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License along
#with this program; if not, write to the Free Software Foundation, Inc.,
#51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from org.json.simple import JsonObject, JsonSimple
import os.path
from java.io import File

class _FascinatorHome:
    root = "."

    def getPath(self):
        return self.root

    def getPath(self, pth):
        return os.path.join(self.root, pth)

    def setPath(self, path):
        self.__class__.__dict__['root'] = path

    def getPathFile(self, path):
        return File(path)

FascinatorHome = _FascinatorHome()



