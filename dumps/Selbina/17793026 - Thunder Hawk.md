# 17793026 - Thunder Hawk

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | Selbina (ID: 248) |
| Block Size       | 1180 bytes        |
| Total Events     | 7                 |
| References Count | 30                |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [80](#event-80)       | 0x0001       |    342 |             56 |
| [81](#event-81)       | 0x0157       |    420 |             56 |
| [82](#event-82)       | 0x02FB       |     66 |             15 |
| [83](#event-83)       | 0x033D       |    117 |             23 |
| [84](#event-84)       | 0x03B2       |     66 |             15 |
| [176](#event-176)     | 0x03F4       |      1 |              1 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x003C      |          60 |
|       1 | 0x1AA8      |        6824 |
|       2 | 0x1AA9      |        6825 |
|       3 | 0x1AAA      |        6826 |
|       4 | 0x1AAB      |        6827 |
|       5 | 0x1AAC      |        6828 |
|       6 | 0x1A5F      |        6751 |
|       7 | 0x0000      |           0 |
|       8 | 0x1AAD      |        6829 |
|       9 | 0x1AAE      |        6830 |
|      10 | 0x1AAF      |        6831 |
|      11 | 0x1AB0      |        6832 |
|      12 | 0x1AB1      |        6833 |
|      13 | 0x1AB2      |        6834 |
|      14 | 0x1AB3      |        6835 |
|      15 | 0x0046      |          70 |
|      16 | 0x0001      |           1 |
|      17 | 0x1AB4      |        6836 |
|      18 | 0x00C8      |         200 |
|      19 | 0x0003      |           3 |
|      20 | 0x0094      |         148 |
|      21 | 0x1ABB      |        6843 |
|      22 | 0x1ABC      |        6844 |
|      23 | 0x0047      |          71 |
|      24 | 0x00C9      |         201 |
|      25 | 0x0002      |           2 |
|      26 | 0x1B58      |        7000 |
|      27 | 0x1B59      |        7001 |
|      28 | 0x1B56      |        6998 |
|      29 | 0x1B57      |        6999 |

## String References

- **6751**: Well? [Of course./Sorry, but I can't.]
- **6824**: I hear about you a lot. People say you do much for Selbina.
- **6825**: I speak for the whole town when I say thank you. Thank you.
- **6826**: Thing is, the turtlebacks are on the move. Word is they're up to no good.
- **6827**: I'm itching to go smash them, but I can't leave the town defenseless.
- **6828**: Maybe you could go instead. What do you say?
- **6829**: Thanks. The turtlebacks often strike merchants headed to our village. Another caravan was attacked just the other day.
- **6830**: They fled, but two of them were taken prisoner.
- **6831**: The turtlebacks prowling outside came from Beadeaux. We think the merchants are held captive there.
- **6832**: Their names are Evrard and Serafin.
- **6833**: They say that the turtlebacks keep prisoners locked up tight. Somewhere in Beadeaux there should be such a place.
- **6834**: The merchants who made it here said that they were different from other turtlebacks. I hope that helps.
- **6835**: I hate asking others to do our job, but please, rescue the two captives. Their families need them.
- **6836**: Oh? Pity... I hoped you would say yes.
- **6843**: We're thankful enough you're safe. We apologize we couldn't help you.
- **6844**: But you did well. Thank you! This is for your service.
- **6998**: This is the mayor's mansion. Our mayor is a good man. Go inside and say hello.
- **6999**: The Valkurm Dunes is Selbina's territory, but our militia is too few to patrol it. It is sad, but you adventurers must keep the sands safe.
- **7000**: Oh, you again. Thanks for all you've done for us. We need all the help we can get.
- **7001**: No reports of trouble recently. For us, no news is good news!

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

### Event 80

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 342 bytes |
| Instructions | 56        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 1D  ...tlk0...#...#.
0020: 03 80 23 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  ..#S........tlk0
0030: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 1D  f..........thk1.
0040: 04 80 23 53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 31  ..#S........thk1
0050: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 32 53  f..........thk2S
0060: F8 FF FF 7F F8 FF FF 7F  74 68 6B 32 66 00 80 F8  ........thk2f...
0070: FF FF 7F F8 FF FF 7F 74  6C 6B 30 1D 05 80 23 5E  .......tlk0...#^
0080: 69 64 6C 30 24 06 80 07  80 07 80 25 02 00 10 07  idl0$......%....
0090: 80 00 28 01 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..(.f..........t
00A0: 6C 6B 30 1D 08 80 23 53  F8 FF FF 7F F8 FF FF 7F  lk0...#S........
00B0: 74 6C 6B 30 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  tlk0f..........t
00C0: 68 6B 31 1D 09 80 23 53  F8 FF FF 7F F8 FF FF 7F  hk1...#S........
00D0: 74 68 6B 31 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  thk1f..........t
00E0: 68 6B 32 53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  hk2S........thk2
00F0: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0100: 0A 80 23 1D 0B 80 23 1D  0C 80 23 1D 0D 80 23 1D  ..#...#...#...#.
0110: 0E 80 23 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  ..#S........tlk0
0120: 03 01 10 0F 80 01 55 01  02 00 10 10 80 00 55 01  ......U.......U.
0130: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 68 6B 31 1D  f..........thk1.
0140: 11 80 23 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 68  ..#f..........th
0150: 6B 32 01 55 01 21 00                              k2.U.!.         
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=6824*)
    → "I hear about you a lot. People say you do much for Selbina."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=6825*)
    → "I speak for the whole town when I say thank you. Thank you."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x1D] PRINT_EVENT_MESSAGE(message_id=6826*)
    → "Thing is, the turtlebacks are on the move. Word is they're up to no good."
  9: 0x0022 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0023 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 11: 0x0030 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
 12: 0x003F [0x1D] PRINT_EVENT_MESSAGE(message_id=6827*)
    → "I'm itching to go smash them, but I can't leave the town defenseless."
 13: 0x0042 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0043 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 15: 0x0050 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
 16: 0x005F [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 17: 0x006C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 18: 0x007B [0x1D] PRINT_EVENT_MESSAGE(message_id=6828*)
    → "Maybe you could go instead. What do you say?"
 19: 0x007E [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x007F [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 21: 0x0084 [0x24] CREATE_DIALOG(message_id=6751*, default_option=0*, option_flags=0*)
    → "Well? [Of course./Sorry, but I can't.]"
 22: 0x008B [0x25] WAIT_DIALOG_SELECT()
 23: 0x008C [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0128
 24: 0x0094 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 25: 0x00A3 [0x1D] PRINT_EVENT_MESSAGE(message_id=6829*)
    → "Thanks. The turtlebacks often strike merchants headed to our village. Another caravan was attacked just the other day."
 26: 0x00A6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x00A7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 28: 0x00B4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
 29: 0x00C3 [0x1D] PRINT_EVENT_MESSAGE(message_id=6830*)
    → "They fled, but two of them were taken prisoner."
 30: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION
 31: 0x00C7 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
 32: 0x00D4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
 33: 0x00E3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
 34: 0x00F0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 35: 0x00FF [0x1D] PRINT_EVENT_MESSAGE(message_id=6831*)
    → "The turtlebacks prowling outside came from Beadeaux. We think the merchants are held captive there."
 36: 0x0102 [0x23] WAIT_FOR_DIALOG_INTERACTION
 37: 0x0103 [0x1D] PRINT_EVENT_MESSAGE(message_id=6832*)
    → "Their names are Evrard and Serafin."
 38: 0x0106 [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x0107 [0x1D] PRINT_EVENT_MESSAGE(message_id=6833*)
    → "They say that the turtlebacks keep prisoners locked up tight. Somewhere in Beadeaux there should be such a place."
 40: 0x010A [0x23] WAIT_FOR_DIALOG_INTERACTION
 41: 0x010B [0x1D] PRINT_EVENT_MESSAGE(message_id=6834*)
    → "The merchants who made it here said that they were different from other turtlebacks. I hope that helps."
 42: 0x010E [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x010F [0x1D] PRINT_EVENT_MESSAGE(message_id=6835*)
    → "I hate asking others to do our job, but please, rescue the two captives. Their families need them."
 44: 0x0112 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0113 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 46: 0x0120 [0x03] Work_Zone[1] = 70*
 47: 0x0125 [0x01] GOTO 0x0155
 48: 0x0128 [0x02] IF !(Work_Zone[0] == 1*) GOTO 0x0155
 49: 0x0130 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
 50: 0x013F [0x1D] PRINT_EVENT_MESSAGE(message_id=6836*)
    → "Oh? Pity... I hoped you would say yes."
 51: 0x0142 [0x23] WAIT_FOR_DIALOG_INTERACTION
 52: 0x0143 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
 53: 0x0152 [0x01] GOTO 0x0155

SUBROUTINE_0155:
 54: 0x0155 [0x21] END_EVENT
 55: 0x0156 [0x00] END_REQSTACK()
```

### Event 81

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0157    |
| Data Size    | 420 bytes |
| Instructions | 56        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0150:                      20  01 42 45 12 80 F0 FF FF          .BE.....
0160: 7F F0 FF FF 7F 66 64 6F  31 07 80 55 12 80 F0 FF  .....fdo1..U....
0170: FF 7F F0 FF FF 7F 66 64  6F 31 46 01 38 13 80 45  ......fdo1F.8..E
0180: 14 80 F0 FF FF 7F F0 FF  FF 7F 73 65 30 30 07 80  ..........se00..
0190: 1C 00 80 29 80 F0 FF FF  7F 0B 27 80 04 80 0F 01  ...)......'.....
01A0: 02 45 12 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  .E..........fdi1
01B0: 07 80 55 14 80 F0 FF FF  7F F0 FF FF 7F 73 65 30  ..U..........se0
01C0: 30 55 12 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 31  0U..........fdi1
01D0: 29 80 03 80 0F 01 02 2A  80 04 80 0F 01 29 80 04  )......*.....)..
01E0: 80 0F 01 03 45 14 80 F0  FF FF 7F F0 FF FF 7F 73  ....E..........s
01F0: 65 30 31 07 80 55 14 80  F0 FF FF 7F F0 FF FF 7F  e01..U..........
0200: 73 65 30 31 1D 15 80 66  00 80 F8 FF FF 7F F8 FF  se01...f........
0210: FF 7F 74 6C 6B 30 4A 04  80 0F 01 F8 FF FF 7F 4A  ..tlk0J........J
0220: 03 80 0F 01 F8 FF FF 7F  6F 76 04 80 0F 01 6F 76  ........ov....ov
0230: 03 80 0F 01 23 53 F8 FF  FF 7F F8 FF FF 7F 74 6C  ....#S........tl
0240: 6B 30 5E 69 64 6C 30 1E  F0 FF FF 7F 6F 70 66 00  k0^idl0.....opf.
0250: 80 F8 FF FF 7F F8 FF FF  7F 74 6C 6B 30 1D 16 80  .........tlk0...
0260: 4A F0 FF FF 7F F8 FF FF  7F 4A 04 80 0F 01 F0 FF  J........J......
0270: FF 7F 4A 03 80 0F 01 F0  FF FF 7F 6F 76 F0 FF FF  ..J........ov...
0280: 7F 6F 76 04 80 0F 01 6F  76 03 80 0F 01 23 53 02  .ov....ov....#S.
0290: 80 0F 01 02 80 0F 01 74  6C 6B 30 29 80 03 80 0F  .......tlk0)....
02A0: 01 03 45 12 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  ..E..........fdo
02B0: 30 07 80 55 12 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0..U..........fd
02C0: 6F 30 29 80 03 80 0F 01  04 29 80 04 80 0F 01 04  o0)......)......
02D0: 46 00 45 12 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  F.E..........fdi
02E0: 30 07 80 03 01 10 17 80  45 18 80 F0 FF FF 7F F0  0.......E.......
02F0: FF FF 7F 71 73 74 63 07  80 21 00                 ...qstc..!.     
```

#### Opcodes

```
  0: 0x0157 [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x0159 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x015A [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  3: 0x016B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
  4: 0x017A [0x46] CAMERA_CONTROL: Disable user control
  5: 0x017C [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
  6: 0x017F [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se00" with entities [LocalPlayer, LocalPlayer], work=[148*, 0*]
  7: 0x0190 [0x1C] WAIT(60* ticks)
  8: 0x0193 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=LocalPlayer, tag_num=0x0B)
  9: 0x019A [0x27] REQ_SET(priority=0x80, entity_id=Evrard (ID: 17793028/0x010F8004), tag_num=0x02)
 10: 0x01A1 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 11: 0x01B2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "se00" with entities [LocalPlayer, LocalPlayer], work=148*
 12: 0x01C1 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 13: 0x01D0 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Serafin (ID: 17793027/0x010F8003), tag_num=0x02)
 14: 0x01D7 [0x2A] GET_REQ_LEVEL(level=128, entity_id=Evrard (ID: 17793028/0x010F8004))
 15: 0x01DD [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Evrard (ID: 17793028/0x010F8004), tag_num=0x03)
 16: 0x01E4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "se01" with entities [LocalPlayer, LocalPlayer], work=[148*, 0*]
 17: 0x01F5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "se01" with entities [LocalPlayer, LocalPlayer], work=148*
 18: 0x0204 [0x1D] PRINT_EVENT_MESSAGE(message_id=6843*)
    → "We're thankful enough you're safe. We apologize we couldn't help you."
 19: 0x0207 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 20: 0x0216 [0x4A] Evrard (ID: 17793028/0x010F8004) looks at EventEntity
 21: 0x021F [0x4A] Serafin (ID: 17793027/0x010F8003) looks at EventEntity
 22: 0x0228 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 23: 0x0229 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Evrard (ID: 17793028/0x010F8004) Render.Flags0 and Render.Flags3 conditions are met
 24: 0x022E [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 25: 0x022F [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Serafin (ID: 17793027/0x010F8003) Render.Flags0 and Render.Flags3 conditions are met
 26: 0x0234 [0x23] WAIT_FOR_DIALOG_INTERACTION
 27: 0x0235 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 28: 0x0242 [0x5E] EventEntity goes idle (kills current action) (animation: "idl0")
 29: 0x0247 [0x1E] EventEntity looks at LocalPlayer and starts talking
 30: 0x024C [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 31: 0x024D [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
 32: 0x024E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 33: 0x025D [0x1D] PRINT_EVENT_MESSAGE(message_id=6844*)
    → "But you did well. Thank you! This is for your service."
 34: 0x0260 [0x4A] LocalPlayer looks at EventEntity
 35: 0x0269 [0x4A] Evrard (ID: 17793028/0x010F8004) looks at LocalPlayer
 36: 0x0272 [0x4A] Serafin (ID: 17793027/0x010F8003) looks at LocalPlayer
 37: 0x027B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 38: 0x027C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 39: 0x0281 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 40: 0x0282 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Evrard (ID: 17793028/0x010F8004) Render.Flags0 and Render.Flags3 conditions are met
 41: 0x0287 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 42: 0x0288 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Serafin (ID: 17793027/0x010F8003) Render.Flags0 and Render.Flags3 conditions are met
 43: 0x028D [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x028E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [Thunder Hawk (ID: 17793026/0x010F8002), Thunder Hawk (ID: 17793026/0x010F8002)]
 45: 0x029B [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Serafin (ID: 17793027/0x010F8003), tag_num=0x03)
 46: 0x02A2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 47: 0x02B3 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
 48: 0x02C2 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Serafin (ID: 17793027/0x010F8003), tag_num=0x04)
 49: 0x02C9 [0x29] REQ_SET_WAIT(priority=0x80, entity_id=Evrard (ID: 17793028/0x010F8004), tag_num=0x04)
 50: 0x02D0 [0x46] CAMERA_CONTROL: Restore default settings
 51: 0x02D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 52: 0x02E3 [0x03] Work_Zone[1] = 71*
 53: 0x02E8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [LocalPlayer, LocalPlayer], work=[201*, 0*]
 54: 0x02F9 [0x21] END_EVENT
 55: 0x02FA [0x00] END_REQSTACK()
```

### Event 82

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x02FB   |
| Data Size    | 66 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
02F0:                                   1E F0 FF FF 7F             .....
0300: 12 00 00 3F 00 00 00 00  19 80 6F 70 66 00 80 F8  ...?......opf...
0310: FF FF 7F F8 FF FF 7F 74  6C 6B 30 02 00 00 07 80  .......tlk0.....
0320: 00 2A 03 1D 1A 80 23 01  2E 03 1D 1B 80 23 53 02  .*....#......#S.
0330: 80 0F 01 02 80 0F 01 74  6C 6B 30 21 00           .......tlk0!.   
```

#### Opcodes

```
  0: 0x02FB [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0300 [0x12] ExtData[1]->WorkLocal[0] = rand()
  2: 0x0303 [0x3F] ExtData[1]->WorkLocal[0] = ExtData[1]->WorkLocal[0] % 2*
  3: 0x030A [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x030B [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x030C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  6: 0x031B [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x032A
  7: 0x0323 [0x1D] PRINT_EVENT_MESSAGE(message_id=7000*)
    → "Oh, you again. Thanks for all you've done for us. We need all the help we can get."
  8: 0x0326 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0327 [0x01] GOTO 0x032E
 10: 0x032A [0x1D] PRINT_EVENT_MESSAGE(message_id=7001*)
    → "No reports of trouble recently. For us, no news is good news!"
 11: 0x032D [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_032E:
 12: 0x032E [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [Thunder Hawk (ID: 17793026/0x010F8002), Thunder Hawk (ID: 17793026/0x010F8002)]
 13: 0x033B [0x21] END_EVENT
 14: 0x033C [0x00] END_REQSTACK()
```

### Event 83

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x033D    |
| Data Size    | 117 bytes |
| Instructions | 23        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0330:                                         1E F0 FF               ...
0340: FF 7F 6F 70 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  ..opf..........t
0350: 68 6B 31 1D 09 80 23 53  F8 FF FF 7F F8 FF FF 7F  hk1...#S........
0360: 74 68 6B 31 66 00 80 F8  FF FF 7F F8 FF FF 7F 74  thk1f..........t
0370: 68 6B 32 53 F8 FF FF 7F  F8 FF FF 7F 74 68 6B 32  hk2S........thk2
0380: 66 00 80 F8 FF FF 7F F8  FF FF 7F 74 6C 6B 30 1D  f..........tlk0.
0390: 0A 80 23 1D 0B 80 23 1D  0C 80 23 1D 0D 80 23 1D  ..#...#...#...#.
03A0: 0E 80 23 53 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  ..#S........tlk0
03B0: 21 00                                             !.              
```

#### Opcodes

```
  0: 0x033D [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0342 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0343 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0344 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [EventEntity, EventEntity], work=60*
  4: 0x0353 [0x1D] PRINT_EVENT_MESSAGE(message_id=6830*)
    → "They fled, but two of them were taken prisoner."
  5: 0x0356 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0357 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk1" with entities [EventEntity, EventEntity]
  7: 0x0364 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [EventEntity, EventEntity], work=60*
  8: 0x0373 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [EventEntity, EventEntity]
  9: 0x0380 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
 10: 0x038F [0x1D] PRINT_EVENT_MESSAGE(message_id=6831*)
    → "The turtlebacks prowling outside came from Beadeaux. We think the merchants are held captive there."
 11: 0x0392 [0x23] WAIT_FOR_DIALOG_INTERACTION
 12: 0x0393 [0x1D] PRINT_EVENT_MESSAGE(message_id=6832*)
    → "Their names are Evrard and Serafin."
 13: 0x0396 [0x23] WAIT_FOR_DIALOG_INTERACTION
 14: 0x0397 [0x1D] PRINT_EVENT_MESSAGE(message_id=6833*)
    → "They say that the turtlebacks keep prisoners locked up tight. Somewhere in Beadeaux there should be such a place."
 15: 0x039A [0x23] WAIT_FOR_DIALOG_INTERACTION
 16: 0x039B [0x1D] PRINT_EVENT_MESSAGE(message_id=6834*)
    → "The merchants who made it here said that they were different from other turtlebacks. I hope that helps."
 17: 0x039E [0x23] WAIT_FOR_DIALOG_INTERACTION
 18: 0x039F [0x1D] PRINT_EVENT_MESSAGE(message_id=6835*)
    → "I hate asking others to do our job, but please, rescue the two captives. Their families need them."
 19: 0x03A2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 20: 0x03A3 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [EventEntity, EventEntity]
 21: 0x03B0 [0x21] END_EVENT
 22: 0x03B1 [0x00] END_REQSTACK()
```

### Event 84

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x03B2   |
| Data Size    | 66 bytes |
| Instructions | 15       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03B0:       1E F0 FF FF 7F 12  00 00 3F 00 00 00 00 19    ........?.....
03C0: 80 6F 70 66 00 80 F8 FF  FF 7F F8 FF FF 7F 74 6C  .opf..........tl
03D0: 6B 30 02 00 00 07 80 00  E1 03 1D 1C 80 23 01 E5  k0...........#..
03E0: 03 1D 1D 80 23 53 02 80  0F 01 02 80 0F 01 74 6C  ....#S........tl
03F0: 6B 30 21 00                                       k0!.            
```

#### Opcodes

```
  0: 0x03B2 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x03B7 [0x12] ExtData[1]->WorkLocal[0] = rand()
  2: 0x03BA [0x3F] ExtData[1]->WorkLocal[0] = ExtData[1]->WorkLocal[0] % 2*
  3: 0x03C1 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  4: 0x03C2 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  5: 0x03C3 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=60*
  6: 0x03D2 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x03E1
  7: 0x03DA [0x1D] PRINT_EVENT_MESSAGE(message_id=6998*)
    → "This is the mayor's mansion. Our mayor is a good man. Go inside and say hello."
  8: 0x03DD [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x03DE [0x01] GOTO 0x03E5
 10: 0x03E1 [0x1D] PRINT_EVENT_MESSAGE(message_id=6999*)
    → "The Valkurm Dunes is Selbina's territory, but our militia is too few to patrol it. It is sad, but you adventurers must keep the sands safe."
 11: 0x03E4 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_03E5:
 12: 0x03E5 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "tlk0" with entities [Thunder Hawk (ID: 17793026/0x010F8002), Thunder Hawk (ID: 17793026/0x010F8002)]
 13: 0x03F2 [0x21] END_EVENT
 14: 0x03F3 [0x00] END_REQSTACK()
```

### Event 176

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x03F4  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
03F0:             00                                        .           
```

#### Opcodes

```
  0: 0x03F4 [0x00] END_REQSTACK()
```
