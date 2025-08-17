# 17809535 - Wistful Bison

## Common Data

| Field            | Value          |
|------------------|----------------|
| Zone             | Norg (ID: 252) |
| Block Size       | 740 bytes      |
| Total Events     | 9              |
| References Count | 39             |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [268](#event-268)     | 0x0001       |     35 |              9 |
| [269](#event-269)     | 0x0024       |    295 |             67 |
| [270](#event-270)     | 0x014B       |     43 |             11 |
| [271](#event-271)     | 0x0176       |     35 |              9 |
| [272](#event-272)     | 0x0199       |     28 |              8 |
| [273](#event-273)     | 0x01B5       |     36 |             10 |
| [274](#event-274)     | 0x01D9       |     28 |              8 |
| [275](#event-275)     | 0x01F5       |     29 |             13 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0014      |          20 |
|       1 | 0x2FCD      |       12237 |
|       2 | 0x2FCE      |       12238 |
|       3 | 0x0876      |        2166 |
|       4 | 0x2FCF      |       12239 |
|       5 | 0x0045      |          69 |
|       6 | 0x2FD0      |       12240 |
|       7 | 0x2FD1      |       12241 |
|       8 | 0x2FD2      |       12242 |
|       9 | 0x0000      |           0 |
|      10 | 0x300D      |       12301 |
|      11 | 0x2FD4      |       12244 |
|      12 | 0x0003      |           3 |
|      13 | 0x0078      |         120 |
|      14 | 0x3012      |       12306 |
|      15 | 0x0001      |           1 |
|      16 | 0x2FD5      |       12245 |
|      17 | 0x2FD6      |       12246 |
|      18 | 0x2FD7      |       12247 |
|      19 | 0x2FD8      |       12248 |
|      20 | 0x2FD9      |       12249 |
|      21 | 0x0022      |          34 |
|      22 | 0x2FDA      |       12250 |
|      23 | 0x2FDB      |       12251 |
|      24 | 0x2FDC      |       12252 |
|      25 | 0x00B4      |         180 |
|      26 | 0x2FDD      |       12253 |
|      27 | 0x2FDE      |       12254 |
|      28 | 0x2FD3      |       12243 |
|      29 | 0x0015      |          21 |
|      30 | 0x2FDF      |       12255 |
|      31 | 0x2FE0      |       12256 |
|      32 | 0x2FE1      |       12257 |
|      33 | 0x2FE2      |       12258 |
|      34 | 0x2FE3      |       12259 |
|      35 | 0x2FE4      |       12260 |
|      36 | 0x2FE5      |       12261 |
|      37 | 0x2FE6      |       12262 |
|      38 | 0x2FE7      |       12263 |

## String References

- **12260**: Well, could a day for greeting visitors be any gloomier? What can I do for you?
- **12261**: Anastase told you to bring me something? Great--not like it will divert my attention from this monotony for long, though.
- **12262**: Other than keeping the waypoints in check, there's not much for me to do out here. Just the same tired routine, week after week...
- **12263**: Tell him that things are going well, but that I really need a break.
- **12301**: Record this fount? [Yes./No.]
- **12306**: Your $3 has been attuned to a geomagnetic fount[ in Selbina/ in Mhaura/ in Rabao/ in Norg]!

## Events

### Event 65535

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0000  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000: 00                                                .               
```

#### Opcodes

```
  0: 0x0000 [0x00] END_REQSTACK()
```

### Event 268

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F 7F C0  0F 01 1C 00 80 1E F0 FF   J..............
0010: FF 7F 2B 7F C0 0F 01 01  80 23 2B 7F C0 0F 01 02  ..+......#+.....
0020: 80 23 21 00                                       .#!.            
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  1: 0x000A [0x1C] WAIT(20* ticks)
  2: 0x000D [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0012 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12237*]:
    → "Hello, there. Terrible day, isn't it? My name's Wistful Bison, and I made the painful trek here from Adoulin."
  4: 0x0019 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x001A [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12238*]:
    → "I'm here on a mission, so I'm not supposed to chat with any old person. I can only talk to those with jobs from Anastase. Sorry."
  6: 0x0021 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0022 [0x21] END_EVENT
  8: 0x0023 [0x00] END_REQSTACK()
```

### Event 269

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0024    |
| Data Size    | 295 bytes |
| Instructions | 66        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0020:             4A F0 FF FF  7F 7F C0 0F 01 1C 00 80      J...........
0030: 1E F0 FF FF 7F 03 02 10  03 80 2B 7F C0 0F 01 04  ..........+.....
0040: 80 23 66 05 80 7F C0 0F  01 7F C0 0F 01 74 6C 6B  .#f..........tlk
0050: 30 2B 7F C0 0F 01 06 80  23 2B 7F C0 0F 01 07 80  0+......#+......
0060: 23 66 05 80 7F C0 0F 01  7F C0 0F 01 74 6C 6B 31  #f..........tlk1
0070: 2B 7F C0 0F 01 08 80 23  03 01 10 09 80 24 0A 80  +......#.....$..
0080: 09 80 09 80 25 02 00 10  09 80 00 34 01 42 03 02  ....%......4.B..
0090: 10 03 80 2B 7F C0 0F 01  0B 80 23 6E F0 FF FF 7F  ...+......#n....
00A0: 0C 80 99 F0 FF FF 7F 1C  0D 80 23 03 03 10 03 80  ..........#.....
00B0: 03 02 10 0C 80 48 0E 80  23 03 01 10 0F 80 03 02  .....H..#.......
00C0: 10 03 80 2B 7F C0 0F 01  10 80 23 2B 7F C0 0F 01  ...+......#+....
00D0: 11 80 23 2B 7F C0 0F 01  12 80 23 2B 7F C0 0F 01  ..#+......#+....
00E0: 13 80 23 2B 7F C0 0F 01  14 80 23 6E F0 FF FF 7F  ..#+......#n....
00F0: 15 80 99 F0 FF FF 7F 1C  0D 80 2B 7F C0 0F 01 16  ..........+.....
0100: 80 23 2B 7F C0 0F 01 17  80 23 6E 7F C0 0F 01 0F  .#+......#n.....
0110: 80 99 7F C0 0F 01 2B 7F  C0 0F 01 18 80 23 1C 19  ......+......#..
0120: 80 2B 7F C0 0F 01 1A 80  23 2B 7F C0 0F 01 1B 80  .+......#+......
0130: 23 01 49 01 02 00 10 0F  80 00 49 01 2B 7F C0 0F  #.I.......I.+...
0140: 01 1C 80 23 21 00 01 49  01 21 00                 ...#!..I.!.     
```

#### Opcodes

```
  0: 0x0024 [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  1: 0x002D [0x1C] WAIT(20* ticks)
  2: 0x0030 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0035 [0x03] Work_Zone[2] = 2166*
  4: 0x003A [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12239*]:
    → "Are you an adventurer? I see you have $6. You got that from Anastase, didn't you?"
  5: 0x0041 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0042 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Wistful Bison (ID: 17809535/0x010FC07F), Wistful Bison (ID: 17809535/0x010FC07F)], work=69*
  7: 0x0051 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12240*]:
    → "If that's the case, I've found where the magnetic field is at its strongest, but..."
  8: 0x0058 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0059 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12241*]:
    → "The person in charge tells me I have to keep fishing up subligaria and leggings from the local waters before he'll let me...never mind. You don't want to hear my depressing stories anyway."
 10: 0x0060 [0x23] WAIT_FOR_DIALOG_INTERACTION
 11: 0x0061 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [Wistful Bison (ID: 17809535/0x010FC07F), Wistful Bison (ID: 17809535/0x010FC07F)], work=69*
 12: 0x0070 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12242*]:
    → "Let's just get this over with. Do you want to record the activity at this spot?"
 13: 0x0077 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0078 [0x03] Work_Zone[1] = 0*
 15: 0x007D [0x24] CREATE_DIALOG(message_id=12301*, default_option=0*, option_flags=0*)
    → "Record this fount? [Yes./No.]"
 16: 0x0084 [0x25] WAIT_DIALOG_SELECT()
 17: 0x0085 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0134
 18: 0x008D [0x42] SET_CLI_EVENT_CANCEL_DATA()
 19: 0x008E [0x03] Work_Zone[2] = 2166*
 20: 0x0093 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12244*]:
    → "<Sigh> Sometimes I can barely work up the energy to do even the simplest task. Put your $3 here, I guess."
 21: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 22: 0x009B [0x6E] LocalPlayer uses emote 3*
 23: 0x00A2 [0x99] Wait for LocalPlayer animation to complete
 24: 0x00A7 [0x1C] WAIT(120* ticks)
 25: 0x00AA [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x00AB [0x03] Work_Zone[3] = 2166*
 27: 0x00B0 [0x03] Work_Zone[2] = 3*
 28: 0x00B5 [0x48] [System] [12306*]:
    → "Your $3 has been attuned to a geomagnetic fount[ in Selbina/ in Mhaura/ in Rabao/ in Norg]!"
 29: 0x00B8 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x00B9 [0x03] Work_Zone[1] = 1*
 31: 0x00BE [0x03] Work_Zone[2] = 2166*
 32: 0x00C3 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12245*]:
    → "Oh, joy...you succeeded. It's now ready to go whenever you are."
 33: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 34: 0x00CB [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12246*]:
    → "I've been told to mind this waypoint, so use it as much as you want. No one ever takes my feelings into account anyway."
 35: 0x00D2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x00D3 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12247*]:
    → "As I'm sure is obvious, my burning passion for adventure led me to join this survey of the Middle Lands. On my way here, though, I <sigh> got lost in a cave. I always get lost."
 37: 0x00DA [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x00DB [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12248*]:
    → "I was able to get out by remembering to put my right hand on the wall and...ugh, you don't care."
 39: 0x00E2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x00E3 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12249*]:
    → "Eventually I wandered here. With all the strange artifacts around, this isn't the worst place I could've ended up."
 41: 0x00EA [0x23] WAIT_FOR_DIALOG_INTERACTION
 42: 0x00EB [0x6E] LocalPlayer uses emote 34*
 43: 0x00F2 [0x99] Wait for LocalPlayer animation to complete
 44: 0x00F7 [0x1C] WAIT(120* ticks)
 45: 0x00FA [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12250*]:
    → "What, Anastase wants a report from me?"
 46: 0x0101 [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x0102 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12251*]:
    → "<Mutter> I guess I don't have a choice... It'd look bad if you reported in and I didn't."
 48: 0x0109 [0x23] WAIT_FOR_DIALOG_INTERACTION
 49: 0x010A [0x6E] Wistful Bison (ID: 17809535/0x010FC07F) uses emote 1*
 50: 0x0111 [0x99] Wait for Wistful Bison (ID: 17809535/0x010FC07F) animation to complete
 51: 0x0116 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12252*]:
    → "Thanks for giving me more work to do, stranger."
 52: 0x011D [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x011E [0x1C] WAIT(180* ticks)
 54: 0x0121 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12253*]:
    → "Oh, and while we're making unnecessary small talk..."
 55: 0x0128 [0x23] WAIT_FOR_DIALOG_INTERACTION
 56: 0x0129 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12254*]:
    → "Can I ask where in the world we are?"
 57: 0x0130 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x0131 [0x01] GOTO 0x0149
 59: 0x0134 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0149
 60: 0x013C [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12243*]:
    → "I see. That's how it always is. I should really be used to this treatment by now."
 61: 0x0143 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x0144 [0x21] END_EVENT
 63: 0x0145 [0x00] END_REQSTACK()

SUBROUTINE_0149:
 64: 0x0149 [0x21] END_EVENT
 65: 0x014A [0x00] END_REQSTACK()
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0146 [0x01] GOTO 0x0149
```

### Event 270

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x014B   |
| Data Size    | 43 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0140:                                   4A F0 FF FF 7F             J....
0150: 7F C0 0F 01 1C 00 80 1E  F0 FF FF 7F 6E 7F C0 0F  ............n...
0160: 01 1D 80 99 7F C0 0F 01  2B 7F C0 0F 01 1E 80 23  ........+......#
0170: 1C 19 80 23 21 00                                 ...#!.          
```

#### Opcodes

```
  0: 0x014B [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  1: 0x0154 [0x1C] WAIT(20* ticks)
  2: 0x0157 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x015C [0x6E] Wistful Bison (ID: 17809535/0x010FC07F) uses emote 21*
  4: 0x0163 [0x99] Wait for Wistful Bison (ID: 17809535/0x010FC07F) animation to complete
  5: 0x0168 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12255*]:
    → "Norg...? That's not where I wanted to go at all..."
  6: 0x016F [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0170 [0x1C] WAIT(180* ticks)
  8: 0x0173 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0174 [0x21] END_EVENT
 10: 0x0175 [0x00] END_REQSTACK()
```

### Event 271

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0176   |
| Data Size    | 35 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0170:                   4A F0  FF FF 7F 7F C0 0F 01 1C        J.........
0180: 00 80 1E F0 FF FF 7F 2B  7F C0 0F 01 1F 80 23 2B  .......+......#+
0190: 7F C0 0F 01 20 80 23 21  00                       .... .#!.       
```

#### Opcodes

```
  0: 0x0176 [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  1: 0x017F [0x1C] WAIT(20* ticks)
  2: 0x0182 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x0187 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12256*]:
    → "That's what happens when all you're told is to set a waypoint where the geomagnetic resonance is strong, though."
  4: 0x018E [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x018F [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12257*]:
    → "I report to the minister of commerce, so I'm supposed to be gathering information on trade in the area..."
  6: 0x0196 [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x0197 [0x21] END_EVENT
  8: 0x0198 [0x00] END_REQSTACK()
```

### Event 272

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0199   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                             42 4A F0 FF FF 7F 7F           BJ.....
01A0: C0 0F 01 1C 00 80 1E F0  FF FF 7F 2B 7F C0 0F 01  ...........+....
01B0: 21 80 23 21 00                                    !.#!.           
```

#### Opcodes

```
  0: 0x0199 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x019A [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  2: 0x01A3 [0x1C] WAIT(20* ticks)
  3: 0x01A6 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x01AB [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12258*]:
    → "Thanks for that. It doesn't help much, but I'll take what I can get."
  5: 0x01B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01B3 [0x21] END_EVENT
  7: 0x01B4 [0x00] END_REQSTACK()
```

### Event 273

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01B5   |
| Data Size    | 36 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01B0:                42 4A F0  FF FF 7F 7F C0 0F 01 1C       BJ.........
01C0: 00 80 1E F0 FF FF 7F 2B  7F C0 0F 01 21 80 23 2B  .......+....!.#+
01D0: 7F C0 0F 01 22 80 23 21  00                       ....".#!.       
```

#### Opcodes

```
  0: 0x01B5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01B6 [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  2: 0x01BF [0x1C] WAIT(20* ticks)
  3: 0x01C2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x01C7 [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12258*]:
    → "Thanks for that. It doesn't help much, but I'll take what I can get."
  5: 0x01CE [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01CF [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12259*]:
    → "Have this in return. I hate fish, so I wasn't going to eat it anyway."
  7: 0x01D6 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x01D7 [0x21] END_EVENT
  9: 0x01D8 [0x00] END_REQSTACK()
```

### Event 274

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01D9   |
| Data Size    | 28 bytes |
| Instructions | 8        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01D0:                             42 4A F0 FF FF 7F 7F           BJ.....
01E0: C0 0F 01 1C 00 80 1E F0  FF FF 7F 2B 7F C0 0F 01  ...........+....
01F0: 22 80 23 21 00                                    ".#!.           
```

#### Opcodes

```
  0: 0x01D9 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01DA [0x4A] LocalPlayer looks at Wistful Bison (ID: 17809535/0x010FC07F)
  2: 0x01E3 [0x1C] WAIT(20* ticks)
  3: 0x01E6 [0x1E] EventEntity looks at LocalPlayer and starts talking
  4: 0x01EB [0x2B] Wistful Bison (ID: 17809535/0x010FC07F) [12259*]:
    → "Have this in return. I hate fish, so I wasn't going to eat it anyway."
  5: 0x01F2 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x01F3 [0x21] END_EVENT
  7: 0x01F4 [0x00] END_REQSTACK()
```

### Event 275

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x01F5   |
| Data Size    | 29 bytes |
| Instructions | 13       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
01F0:                42 1E F0  FF FF 7F 1D 23 80 23 1D       B......#.#.
0200: 24 80 23 1D 25 80 23 1D  26 80 23 03 01 10 0F 80  $.#.%.#.&.#.....
0210: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x01F5 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x01F6 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x01FB [0x1D] PRINT_EVENT_MESSAGE(message_id=12260*)
    → "Well, could a day for greeting visitors be any gloomier? What can I do for you?"
  3: 0x01FE [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x01FF [0x1D] PRINT_EVENT_MESSAGE(message_id=12261*)
    → "Anastase told you to bring me something? Great--not like it will divert my attention from this monotony for long, though."
  5: 0x0202 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0203 [0x1D] PRINT_EVENT_MESSAGE(message_id=12262*)
    → "Other than keeping the waypoints in check, there's not much for me to do out here. Just the same tired routine, week after week..."
  7: 0x0206 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x0207 [0x1D] PRINT_EVENT_MESSAGE(message_id=12263*)
    → "Tell him that things are going well, but that I really need a break."
  9: 0x020A [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x020B [0x03] Work_Zone[1] = 1*
 11: 0x0210 [0x21] END_EVENT
 12: 0x0211 [0x00] END_REQSTACK()
```
