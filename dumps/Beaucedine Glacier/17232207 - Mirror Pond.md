# 17232207 - Mirror Pond

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | Beaucedine Glacier (ID: 111) |
| Block Size       | 852 bytes                    |
| Total Events     | 2                            |
| References Count | 25                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [100](#event-100)     | 0x0001       |    724 |             98 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x00FF      |         255 |
|       1 | 0x0002      |           2 |
|       2 | 0x009F      |         159 |
|       3 | 0x000F      |          15 |
|       4 | 0x000A      |          10 |
|       5 | 0x000B      |          11 |
|       6 | 0x0003      |           3 |
|       7 | 0x0000      |           0 |
|       8 | 0x001E      |          30 |
|       9 | 0x1D0F      |        7439 |
|      10 | 0x1D10      |        7440 |
|      11 | 0x0BC9      |        3017 |
|      12 | 0x1D11      |        7441 |
|      13 | 0x1D12      |        7442 |
|      14 | 0x1D13      |        7443 |
|      15 | 0x1D14      |        7444 |
|      16 | 0x1D15      |        7445 |
|      17 | 0x1D16      |        7446 |
|      18 | 0x1D17      |        7447 |
|      19 | 0x1D18      |        7448 |
|      20 | 0x004B      |          75 |
|      21 | 0x005A      |          90 |
|      22 | 0x0065      |         101 |
|      23 | 0x0067      |         103 |
|      24 | 0x00C8      |         200 |

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

### Event 100

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 724 bytes |
| Instructions | 95        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 46 01 1A 72 02 77  00 80 01 80 5C 00 02 80   BF..r.w....\...
0010: 5C 01 02 80 5C 02 02 80  5C 03 02 80 1C 03 80 66  \...\...\......f
0020: 04 80 50 F1 06 01 50 F1  06 01 00 FE FE FE 66 05  ..P...P.......f.
0030: 80 50 F1 06 01 50 F1 06  01 00 FE FE FE 38 06 80  .P...P.......8..
0040: 27 10 F0 FF FF 7F 02 45  05 80 F0 FF FF 7F F0 FF  '......E........
0050: FF 7F 73 67 30 31 07 80  1A 93 02 2A 10 F0 FF FF  ..sg01.....*....
0060: 7F 55 05 80 F0 FF FF 7F  F0 FF FF 7F 73 67 30 31  .U..........sg01
0070: 27 10 50 F1 06 01 02 45  05 80 F0 FF FF 7F F0 FF  '.P....E........
0080: FF 7F 73 67 30 32 07 80  55 05 80 F0 FF FF 7F F0  ..sg02..U.......
0090: FF FF 7F 73 67 30 32 45  05 80 F0 FF FF 7F F0 FF  ...sg02E........
00A0: FF 7F 73 67 30 33 07 80  1C 08 80 2B 50 F1 06 01  ..sg03.....+P...
00B0: 09 80 23 1A 72 02 1C 03  80 6B 69 64 6C 30 F0 FF  ..#.r....kidl0..
00C0: FF 7F 4A F0 FF FF 7F 50  F1 06 01 6F 76 F0 FF FF  ..J....P...ov...
00D0: 7F 27 10 50 F1 06 01 03  45 05 80 F0 FF FF 7F F0  .'.P....E.......
00E0: FF FF 7F 73 67 30 34 07  80 1A 93 02 2A 10 50 F1  ...sg04.....*.P.
00F0: 06 01 55 05 80 F0 FF FF  7F F0 FF FF 7F 73 67 30  ..U..........sg0
0100: 34 45 05 80 F0 FF FF 7F  F0 FF FF 7F 73 67 30 35  4E..........sg05
0110: 07 80 1C 08 80 2B 50 F1  06 01 0A 80 23 4B 50 F1  .....+P.....#KP.
0120: 06 01 0B 80 6F 76 50 F1  06 01 1C 03 80 66 05 80  ....ovP......f..
0130: 50 F1 06 01 50 F1 06 01  75 74 6C 30 2B 50 F1 06  P...P...utl0+P..
0140: 01 0C 80 23 2B 50 F1 06  01 0D 80 23 66 05 80 50  ...#+P.....#f..P
0150: F1 06 01 50 F1 06 01 75  74 6C 31 53 50 F1 06 01  ...P...utl1SP...
0160: 50 F1 06 01 75 74 6C 31  1C 08 80 2B 50 F1 06 01  P...utl1...+P...
0170: 0E 80 23 53 50 F1 06 01  50 F1 06 01 75 6E 7A 30  ..#SP...P...unz0
0180: 45 05 80 F0 FF FF 7F F0  FF FF 7F 73 67 30 36 07  E..........sg06.
0190: 80 66 04 80 50 F1 06 01  50 F1 06 01 74 68 6B 31  .f..P...P...thk1
01A0: 2B 50 F1 06 01 0F 80 23  2B 50 F1 06 01 10 80 23  +P.....#+P.....#
01B0: 2B 50 F1 06 01 11 80 23  2B 50 F1 06 01 12 80 23  +P.....#+P.....#
01C0: 66 04 80 50 F1 06 01 50  F1 06 01 74 68 6B 32 53  f..P...P...thk2S
01D0: 50 F1 06 01 50 F1 06 01  74 68 6B 32 55 05 80 F0  P...P...thk2U...
01E0: FF FF 7F F0 FF FF 7F 73  67 30 36 45 05 80 F0 FF  .......sg06E....
01F0: FF 7F F0 FF FF 7F 73 67  30 37 07 80 4A 50 F1 06  ......sg07..JP..
0200: 01 F0 FF FF 7F 6F 76 50  F1 06 01 2B 50 F1 06 01  .....ovP...+P...
0210: 13 80 23 66 05 80 50 F1  06 01 50 F1 06 01 6B 61  ..#f..P...P...ka
0220: 73 30 1C 14 80 1A B4 02  1C 15 80 5C 00 07 80 5C  s0.........\...\
0230: 01 07 80 5C 02 16 80 5C  03 17 80 78 45 18 80 F0  ...\...\...xE...
0240: FF FF 7F F0 FF FF 7F 66  64 69 32 07 80 46 00 21  .......fdi2..F.!
0250: 00 45 18 80 F0 FF FF 7F  F0 FF FF 7F 66 64 69 30  .E..........fdi0
0260: 07 80 55 18 80 F0 FF FF  7F F0 FF FF 7F 66 64 69  ..U..........fdi
0270: 30 1B 45 18 80 F0 FF FF  7F F0 FF FF 7F 66 64 6F  0.E..........fdo
0280: 30 07 80 55 18 80 F0 FF  FF 7F F0 FF FF 7F 66 64  0..U..........fd
0290: 6F 30 1B 45 18 80 F0 FF  FF 7F F0 FF FF 7F 66 64  o0.E..........fd
02A0: 69 31 07 80 55 18 80 F0  FF FF 7F F0 FF FF 7F 66  i1..U..........f
02B0: 64 69 31 1B 45 18 80 F0  FF FF 7F F0 FF FF 7F 66  di1.E..........f
02C0: 64 6F 31 07 80 55 18 80  F0 FF FF 7F F0 FF FF 7F  do1..U..........
02D0: 66 64 6F 31 1B                                    fdo1.           
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x46] CAMERA_CONTROL: Disable user control
  2: 0x0004 [0x1A] CALL_SUBROUTINE(address=0x0272)
  3: 0x0007 [0x77] SET_EVENT_TIME_WEATHER(hour=255*, weather=2*)
  4: 0x000C [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 159*
  5: 0x0010 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 159*
  6: 0x0014 [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 159*
  7: 0x0018 [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 159*
  8: 0x001C [0x1C] WAIT(15* ticks)
  9: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFEFEFE00 with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=10*
 10: 0x002E [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler 0xFEFEFE00 with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=11*
 11: 0x003D [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 12: 0x0040 [0x27] REQ_SET(priority=0x10, entity_id=LocalPlayer, tag_num=0x02)
 13: 0x0047 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg01" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 14: 0x0058 [0x1A] CALL_SUBROUTINE(address=0x0293)
 15: 0x005B [0x2A] GET_REQ_LEVEL(level=16, entity_id=LocalPlayer)
 16: 0x0061 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "sg01" with entities [LocalPlayer, LocalPlayer], work=11*
 17: 0x0070 [0x27] REQ_SET(priority=0x10, entity_id=Dariah (ID: 17232208/0x0106F150), tag_num=0x02)
 18: 0x0077 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg02" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 19: 0x0088 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "sg02" with entities [LocalPlayer, LocalPlayer], work=11*
 20: 0x0097 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg03" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 21: 0x00A8 [0x1C] WAIT(30* ticks)
 22: 0x00AB [0x2B] Dariah (ID: 17232208/0x0106F150) [7439*]:
    → "Hey! What are you doing there?"
 23: 0x00B2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 24: 0x00B3 [0x1A] CALL_SUBROUTINE(address=0x0272)
 25: 0x00B6 [0x1C] WAIT(15* ticks)
 26: 0x00B9 [0x6B] STOP_AND_IDLE: LocalPlayer stops current action and resets to idle (animation="idl0")
 27: 0x00C2 [0x4A] LocalPlayer looks at Dariah (ID: 17232208/0x0106F150)
 28: 0x00CB [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 29: 0x00CC [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
 30: 0x00D1 [0x27] REQ_SET(priority=0x10, entity_id=Dariah (ID: 17232208/0x0106F150), tag_num=0x03)
 31: 0x00D8 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg04" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 32: 0x00E9 [0x1A] CALL_SUBROUTINE(address=0x0293)
 33: 0x00EC [0x2A] GET_REQ_LEVEL(level=16, entity_id=Dariah (ID: 17232208/0x0106F150))
 34: 0x00F2 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "sg04" with entities [LocalPlayer, LocalPlayer], work=11*
 35: 0x0101 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg05" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 36: 0x0112 [0x1C] WAIT(30* ticks)
 37: 0x0115 [0x2B] Dariah (ID: 17232208/0x0106F150) [7440*]:
    → "Carmelo asked you? You mean he's still..."
 38: 0x011C [0x23] WAIT_FOR_DIALOG_INTERACTION
 39: 0x011D [0x4B] UPDATE_ENTITY_YAW(entity=Dariah (ID: 17232208/0x0106F150), yaw=16.6°*)
 40: 0x0124 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 41: 0x0125 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dariah (ID: 17232208/0x0106F150) Render.Flags0 and Render.Flags3 conditions are met
 42: 0x012A [0x1C] WAIT(15* ticks)
 43: 0x012D [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "utl0" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=11*
 44: 0x013C [0x2B] Dariah (ID: 17232208/0x0106F150) [7441*]:
    → "Yes, I am the woman he seeks. Why did I leave him? Let's just say that the hands of his clock were about to break."
 45: 0x0143 [0x23] WAIT_FOR_DIALOG_INTERACTION
 46: 0x0144 [0x2B] Dariah (ID: 17232208/0x0106F150) [7442*]:
    → "In those days, he would do anything to make me happy. Anything! He even sold the one thing that brought us together to buy me something that would make me more happy."
 47: 0x014B [0x23] WAIT_FOR_DIALOG_INTERACTION
 48: 0x014C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "utl1" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=11*
 49: 0x015B [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "utl1" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)]
 50: 0x0168 [0x1C] WAIT(30* ticks)
 51: 0x016B [0x2B] Dariah (ID: 17232208/0x0106F150) [7443*]:
    → "I'm not mad about that, it's just that...I felt that if I had stayed, he would have thrown away everything--all that he cherished, all that he was--just for me."
 52: 0x0172 [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x0173 [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "unz0" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)]
 54: 0x0180 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg06" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 55: 0x0191 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk1" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=10*
 56: 0x01A0 [0x2B] Dariah (ID: 17232208/0x0106F150) [7444*]:
    → "I feared he would throw away his future for the sake of our present. Eventually, his time would have come to a stop."
 57: 0x01A7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 58: 0x01A8 [0x2B] Dariah (ID: 17232208/0x0106F150) [7445*]:
    → "I told him that we were like the hands of a clock... That even if we parted, we would meet again."
 59: 0x01AF [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x01B0 [0x2B] Dariah (ID: 17232208/0x0106F150) [7446*]:
    → "But he wanted us to stay where both hands met...even if that meant breaking the gears that kept us in motion."
 61: 0x01B7 [0x23] WAIT_FOR_DIALOG_INTERACTION
 62: 0x01B8 [0x2B] Dariah (ID: 17232208/0x0106F150) [7447*]:
    → "Try to stop time...and you'll only break the hands of the clock."
 63: 0x01BF [0x23] WAIT_FOR_DIALOG_INTERACTION
 64: 0x01C0 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "thk2" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=10*
 65: 0x01CF [0x53] WAIT_SCHEDULER_TASK: Wait for scheduler "thk2" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)]
 66: 0x01DC [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "sg06" with entities [LocalPlayer, LocalPlayer], work=11*
 67: 0x01EB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "sg07" with entities [LocalPlayer, LocalPlayer], work=[11*, 0*]
 68: 0x01FC [0x4A] Dariah (ID: 17232208/0x0106F150) looks at LocalPlayer
 69: 0x0205 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 70: 0x0206 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Dariah (ID: 17232208/0x0106F150) Render.Flags0 and Render.Flags3 conditions are met
 71: 0x020B [0x2B] Dariah (ID: 17232208/0x0106F150) [7448*]:
    → "Tell him that as long as we live, we will meet again--as long as the hands of the clock are moving."
 72: 0x0212 [0x23] WAIT_FOR_DIALOG_INTERACTION
 73: 0x0213 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "kas0" with entities [Dariah (ID: 17232208/0x0106F150), Dariah (ID: 17232208/0x0106F150)], work=11*
 74: 0x0222 [0x1C] WAIT(75* ticks)
 75: 0x0225 [0x1A] CALL_SUBROUTINE(address=0x02B4)
 76: 0x0228 [0x1C] WAIT(90* ticks)
 77: 0x022B [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 0*
 78: 0x022F [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 0*
 79: 0x0233 [0x5C] MUSIC_CONTROL: Set Combat (Solo) music to song 101*
 80: 0x0237 [0x5C] MUSIC_CONTROL: Set Combat (Party) music to song 103*
 81: 0x023B [0x78] ENABLE_GAME_TIMER_RESET_WEATHER()
 82: 0x023C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 83: 0x024D [0x46] CAMERA_CONTROL: Restore default settings
 84: 0x024F [0x21] END_EVENT
 85: 0x0250 [0x00] END_REQSTACK()

SUBROUTINE_0272:
 86: 0x0272 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 87: 0x0283 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo0" with entities [LocalPlayer, LocalPlayer], work=200*
 88: 0x0292 [0x1B] RETURN

SUBROUTINE_0293:
 89: 0x0293 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 90: 0x02A4 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=200*
 91: 0x02B3 [0x1B] RETURN

SUBROUTINE_02B4:
 92: 0x02B4 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 93: 0x02C5 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=200*
 94: 0x02D4 [0x1B] RETURN
```

#### Data or dead code:

```
# Dead code (unreachable instructions):
     0x0251 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
     0x0262 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "fdi0" with entities [LocalPlayer, LocalPlayer], work=200*
     0x0271 [0x1B] RETURN
```
