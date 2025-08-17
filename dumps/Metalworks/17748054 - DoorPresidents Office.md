# 17748054 - DoorPresidents Office

## Common Data

| Field            | Value                |
|------------------|----------------------|
| Zone             | Metalworks (ID: 237) |
| Block Size       | 1596 bytes           |
| Total Events     | 17                   |
| References Count | 48                   |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [722](#event-722)        | 0x0001       |      2 |              2 |
| [713](#event-713)        | 0x0003       |      1 |              1 |
| [604](#event-604)        | 0x0004       |    147 |             35 |
| [715](#event-715)        | 0x0097       |      1 |              1 |
| [65535.1](#event-655351) | 0x0098       |      2 |              2 |
| [65535.2](#event-655352) | 0x009A       |      2 |              2 |
| [720](#event-720)        | 0x009C       |      1 |              1 |
| [603](#event-603)        | 0x009D       |   1154 |            153 |
| [780](#event-780)        | 0x051F       |      1 |              1 |
| [782](#event-782)        | 0x0520       |      1 |              1 |
| [829](#event-829)        | 0x0521       |      1 |              1 |
| [968](#event-968)        | 0x0522       |      1 |              1 |
| [1051](#event-1051)      | 0x0523       |      2 |              2 |
| [1052](#event-1052)      | 0x0525       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x17588     |       95624 |
|       1 | 0x16F30     |       94000 |
|       2 | 0xFFFFF448  |  4294964296 |
|       3 | 0x0BB8      |        3000 |
|       4 | 0x1F37      |        7991 |
|       5 | 0x1F38      |        7992 |
|       6 | 0x0000      |           0 |
|       7 | 0x001E      |          30 |
|       8 | 0x003C      |          60 |
|       9 | 0x1F39      |        7993 |
|      10 | 0x012F      |         303 |
|      11 | 0x00C8      |         200 |
|      12 | 0x0078      |         120 |
|      13 | 0x0003      |           3 |
|      14 | 0x0089      |         137 |
|      15 | 0x1F07      |        7943 |
|      16 | 0x1F08      |        7944 |
|      17 | 0x1F09      |        7945 |
|      18 | 0x1F0A      |        7946 |
|      19 | 0x006E      |         110 |
|      20 | 0x1F0B      |        7947 |
|      21 | 0x1F0C      |        7948 |
|      22 | 0x1F0D      |        7949 |
|      23 | 0x0096      |         150 |
|      24 | 0x1F0E      |        7950 |
|      25 | 0x1F0F      |        7951 |
|      26 | 0x0014      |          20 |
|      27 | 0x1F10      |        7952 |
|      28 | 0x1F11      |        7953 |
|      29 | 0x0006      |           6 |
|      30 | 0x1F12      |        7954 |
|      31 | 0x1F13      |        7955 |
|      32 | 0x006F      |         111 |
|      33 | 0x1F14      |        7956 |
|      34 | 0x1F15      |        7957 |
|      35 | 0x1F16      |        7958 |
|      36 | 0x1F17      |        7959 |
|      37 | 0x1F18      |        7960 |
|      38 | 0x1F19      |        7961 |
|      39 | 0x0800      |        2048 |
|      40 | 0x1F1A      |        7962 |
|      41 | 0x1F1B      |        7963 |
|      42 | 0x1F1C      |        7964 |
|      43 | 0x1F1D      |        7965 |
|      44 | 0x000A      |          10 |
|      45 | 0x00F0      |         240 |
|      46 | 0x009A      |         154 |
|      47 | 0x00C9      |         201 |

## String References

- **7992**: Enter the President's Office? [Yes./No.]
- **7993**: Exit the President's Office? [Yes./No.]

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

### Event 722

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4C 00                                           L.             
```

#### Opcodes

```
  0: 0x0001 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0002 [0x00] END_REQSTACK()
```

### Event 713

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0003  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:          00                                          .            
```

#### Opcodes

```
  0: 0x0003 [0x00] END_REQSTACK()
```

### Event 604

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0004    |
| Data Size    | 147 bytes |
| Instructions | 35        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:             3B F0 FF FF  7F 00 00 02 00 01 00 02      ;...........
0010: 00 00 00 80 03 6F 00 02  00 00 01 80 02 35 00 02  .....o.......5..
0020: 02 00 02 80 03 2A 00 01  6F 00 02 02 00 03 80 02  .....*..o.......
0030: 35 00 01 6F 00 4A 30 D0  0E 01 F0 FF FF 7F 2B 30  5..o.J0.......+0
0040: D0 0E 01 04 80 23 24 05  80 06 80 06 80 25 02 00  .....#$......%..
0050: 10 06 80 00 6C 00 46 01  4C 1C 07 80 29 0A F0 FF  ....l.F.L...)...
0060: FF 7F 1E 4D 1C 08 80 46  00 01 6C 00 01 95 00 24  ...M...F..l....$
0070: 09 80 06 80 06 80 25 02  00 10 06 80 00 95 00 46  ......%........F
0080: 01 4C 1C 07 80 29 0A F0  FF FF 7F 1F 4D 1C 08 80  .L...)......M...
0090: 46 00 01 95 00 21 00                              F....!.         
```

#### Opcodes

```
  0: 0x0004 [0x3B] GET_ENTITY_POSITION(entity=LocalPlayer, x_destination=ExtData[1]->WorkLocal[0], y_destination=ExtData[1]->WorkLocal[2], z_destination=ExtData[1]->WorkLocal[1])
  1: 0x000F [0x02] IF !(ExtData[1]->WorkLocal[0] >= 95624*) GOTO 0x006F
  2: 0x0017 [0x02] IF !(ExtData[1]->WorkLocal[0] <= 94000*) GOTO 0x0035
  3: 0x001F [0x02] IF !(ExtData[1]->WorkLocal[2] >= 4294964296*) GOTO 0x002A
  4: 0x0027 [0x01] GOTO 0x006F
  5: 0x002A [0x02] IF !(ExtData[1]->WorkLocal[2] <= 3000*) GOTO 0x0035
  6: 0x0032 [0x01] GOTO 0x006F
  7: 0x0035 [0x4A] Iron Eater (ID: 17748016/0x010ED030) looks at LocalPlayer
  8: 0x003E [0x2B] Iron Eater (ID: 17748016/0x010ED030) [7991*]:
    → "These doors lead to the President's Office."
  9: 0x0045 [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x0046 [0x24] CREATE_DIALOG(message_id=7992*, default_option=0*, option_flags=0*)
    → "Enter the President's Office? [Yes./No.]"
 11: 0x004D [0x25] WAIT_DIALOG_SELECT()
 12: 0x004E [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x006C
 13: 0x0056 [0x46] CAMERA_CONTROL: Disable user control
 14: 0x0058 [0x4C] EventEntity->StatusEvent = 8 // Open door
 15: 0x0059 [0x1C] WAIT(30* ticks)
 16: 0x005C [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1E)
 17: 0x0063 [0x4D] EventEntity->StatusEvent = 9 // Close door
 18: 0x0064 [0x1C] WAIT(60* ticks)
 19: 0x0067 [0x46] CAMERA_CONTROL: Restore default settings
 20: 0x0069 [0x01] GOTO 0x006C

SUBROUTINE_006C:
 21: 0x006C [0x01] GOTO 0x0095

SUBROUTINE_006F:
 22: 0x006F [0x24] CREATE_DIALOG(message_id=7993*, default_option=0*, option_flags=0*)
    → "Exit the President's Office? [Yes./No.]"
 23: 0x0076 [0x25] WAIT_DIALOG_SELECT()
 24: 0x0077 [0x02] IF !(Work_Zone[0] == 0*) GOTO 0x0095
 25: 0x007F [0x46] CAMERA_CONTROL: Disable user control
 26: 0x0081 [0x4C] EventEntity->StatusEvent = 8 // Open door
 27: 0x0082 [0x1C] WAIT(30* ticks)
 28: 0x0085 [0x29] REQ_SET_WAIT(priority=0x0A, entity_id=LocalPlayer, tag_num=0x1F)
 29: 0x008C [0x4D] EventEntity->StatusEvent = 9 // Close door
 30: 0x008D [0x1C] WAIT(60* ticks)
 31: 0x0090 [0x46] CAMERA_CONTROL: Restore default settings
 32: 0x0092 [0x01] GOTO 0x0095

SUBROUTINE_0095:
 33: 0x0095 [0x21] END_EVENT
 34: 0x0096 [0x00] END_REQSTACK()
```

### Event 715

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0097  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                      00                                  .        
```

#### Opcodes

```
  0: 0x0097 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0098  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                          4C 00                            L.      
```

#### Opcodes

```
  0: 0x0098 [0x4C] EventEntity->StatusEvent = 8 // Open door
  1: 0x0099 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009A  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                4D 00                        M.    
```

#### Opcodes

```
  0: 0x009A [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x009B [0x00] END_REQSTACK()
```

### Event 720

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x009C  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                      00                       .   
```

#### Opcodes

```
  0: 0x009C [0x00] END_REQSTACK()
```

### Event 603

#### Metadata

| Field        | Value      |
|--------------|------------|
| Entrypoint   | 0x009D     |
| Data Size    | 1154 bytes |
| Instructions | 153        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0090:                                         42 75 00               Bu.
00A0: 0A 80 75 01 4C 5D 06 80  08 80 45 0B 80 F0 FF FF  ..u.L]....E.....
00B0: 7F F0 FF FF 7F 66 64 6F  31 06 80 1C 08 80 5C 00  .....fdo1.....\.
00C0: 0C 80 5C 01 0C 80 46 01  38 0D 80 27 0A F0 FF FF  ..\...F.8..'....
00D0: 7F 17 45 0E 80 F0 FF FF  7F F0 FF FF 7F 73 30 36  ..E..........s06
00E0: 36 06 80 45 0B 80 F0 FF  FF 7F F0 FF FF 7F 66 64  6..E..........fd
00F0: 69 31 06 80 4A 2E D0 0E  01 F0 FF FF 7F 1C 08 80  i1..J...........
0100: 1C 0C 80 5B 0B 80 2E D0  0E 01 2E D0 0E 01 74 6C  ...[..........tl
0110: 62 30 79 00 F0 FF FF 7F  2E D0 0E 01 2B 2E D0 0E  b0y.........+...
0120: 01 0F 80 23 5B 0B 80 2E  D0 0E 01 2E D0 0E 01 65  ...#[..........e
0130: 76 30 30 27 0A 2B D0 0E  01 11 79 00 F0 FF FF 7F  v00'.+....y.....
0140: 2B D0 0E 01 2B 2B D0 0E  01 10 80 23 5B 0B 80 2E  +...++.....#[...
0150: D0 0E 01 2E D0 0E 01 69  62 30 31 55 0E 80 F0 FF  .......ib01U....
0160: FF 7F F0 FF FF 7F 73 30  36 36 2B 2E D0 0E 01 11  ......s066+.....
0170: 80 23 2A 0A 2B D0 0E 01  27 0A 18 D0 0E 01 17 1C  .#*.+...'.......
0180: 07 80 79 00 F0 FF FF 7F  18 D0 0E 01 79 00 2B D0  ..y.........y.+.
0190: 0E 01 18 D0 0E 01 45 0E  80 F0 FF FF 7F F0 FF FF  ......E.........
01A0: 7F 73 30 36 37 06 80 2B  18 D0 0E 01 12 80 23 4A  .s067..+......#J
01B0: 2B D0 0E 01 2E D0 0E 01  6F 76 2B D0 0E 01 5B 13  +.......ov+...[.
01C0: 80 2B D0 0E 01 2B D0 0E  01 74 6C 6B 30 2B 2B D0  .+...+...tlk0++.
01D0: 0E 01 14 80 23 5B 13 80  2B D0 0E 01 2B D0 0E 01  ....#[..+...+...
01E0: 74 6C 6B 31 27 0A 2A D0  0E 01 15 1C 07 80 45 0E  tlk1'.*.......E.
01F0: 80 F0 FF FF 7F F0 FF FF  7F 73 30 36 38 06 80 2B  .........s068..+
0200: 2A D0 0E 01 15 80 23 2A  0A 2A D0 0E 01 79 00 2A  *.....#*.*...y.*
0210: D0 0E 01 F0 FF FF 7F 2B  2A D0 0E 01 16 80 23 5B  .......+*.....#[
0220: 17 80 2A D0 0E 01 2A D0  0E 01 74 6C 6B 30 2B 2A  ..*...*...tlk0+*
0230: D0 0E 01 18 80 23 5B 17  80 2A D0 0E 01 2A D0 0E  .....#[..*...*..
0240: 01 74 6C 6B 31 2B 2A D0  0E 01 19 80 23 79 00 2B  .tlk1+*.....#y.+
0250: D0 0E 01 F0 FF FF 7F 27  0A 18 D0 0E 01 18 1C 1A  .......'........
0260: 80 2B 18 D0 0E 01 1B 80  23 5B 13 80 2B D0 0E 01  .+......#[..+...
0270: 2B D0 0E 01 74 6C 6B 30  2B 2B D0 0E 01 1C 80 23  +...tlk0++.....#
0280: 5B 13 80 2B D0 0E 01 2B  D0 0E 01 74 6C 6B 31 7D  [..+...+...tlk1}
0290: 1D 80 1C 0C 80 45 0B 80  F0 FF FF 7F F0 FF FF 7F  .....E..........
02A0: 66 64 6F 32 06 80 1C 0C  80 45 0E 80 F0 FF FF 7F  fdo2.....E......
02B0: F0 FF FF 7F 73 30 36 39  06 80 45 0B 80 F0 FF FF  ....s069..E.....
02C0: 7F F0 FF FF 7F 66 64 69  32 06 80 4D 27 0A F0 FF  .....fdi2..M'...
02D0: FF 7F 19 27 0A 2B D0 0E  01 12 1C 0C 80 2B 2B D0  ...'.+.......++.
02E0: 0E 01 1E 80 23 2A 0A 2B  D0 0E 01 4A 2B D0 0E 01  ....#*.+...J+...
02F0: F0 FF FF 7F 79 00 F0 FF  FF 7F 2B D0 0E 01 2B 2B  ....y.....+...++
0300: D0 0E 01 1F 80 23 5B 20  80 2B D0 0E 01 2B D0 0E  .....#[ .+...+..
0310: 01 74 6C 6B 30 2B 2B D0  0E 01 21 80 23 55 0E 80  .tlk0++...!.#U..
0320: F0 FF FF 7F F0 FF FF 7F  73 30 36 39 45 0E 80 F0  ........s069E...
0330: FF FF 7F F0 FF FF 7F 73  30 37 30 06 80 2B 2B D0  .......s070..++.
0340: 0E 01 22 80 23 5B 20 80  2B D0 0E 01 2B D0 0E 01  ..".#[ .+...+...
0350: 74 6C 6B 31 27 0A 18 D0  0E 01 19 1C 0C 80 2B 18  tlk1'.........+.
0360: D0 0E 01 23 80 23 27 0A  2E D0 0E 01 19 4A 2B D0  ...#.#'......J+.
0370: 0E 01 18 D0 0E 01 2B 2B  D0 0E 01 24 80 23 2A 0A  ......++...$.#*.
0380: 2E D0 0E 01 5B 0B 80 2E  D0 0E 01 2E D0 0E 01 74  ....[..........t
0390: 6C 61 30 79 00 2B D0 0E  01 2E D0 0E 01 2B 2E D0  la0y.+.......+..
03A0: 0E 01 25 80 23 5B 0B 80  2E D0 0E 01 2E D0 0E 01  ..%.#[..........
03B0: 74 6C 61 31 66 06 80 18  D0 0E 01 18 D0 0E 01 74  tla1f..........t
03C0: 6C 6B 30 2B 18 D0 0E 01  26 80 23 66 06 80 18 D0  lk0+....&.#f....
03D0: 0E 01 18 D0 0E 01 74 65  6E 30 7B 2B D0 0E 01 4B  ......ten0{+...K
03E0: 2B D0 0E 01 27 80 55 0E  80 F0 FF FF 7F F0 FF FF  +...'.U.........
03F0: 7F 73 30 37 30 45 0E 80  F0 FF FF 7F F0 FF FF 7F  .s070E..........
0400: 73 30 37 31 06 80 1C 07  80 5B 20 80 2B D0 0E 01  s071.....[ .+...
0410: 2B D0 0E 01 6F 6D 6F 30  2B 2B D0 0E 01 28 80 23  +...omo0++...(.#
0420: 2B 2B D0 0E 01 29 80 23  2B 2B D0 0E 01 2A 80 23  ++...).#++...*.#
0430: 5B 20 80 2B D0 0E 01 2B  D0 0E 01 6F 6D 6F 31 2B  [ .+...+...omo1+
0440: 2B D0 0E 01 2B 80 23 1C  2C 80 79 00 2E D0 0E 01  +...+.#.,.y.....
0450: 18 D0 0E 01 1C 07 80 79  00 18 D0 0E 01 2E D0 0E  .......y........
0460: 01 1C 1A 80 5B 0B 80 2E  D0 0E 01 2E D0 0E 01 6E  ....[..........n
0470: 6F 74 30 1C 1A 80 79 00  F0 FF FF 7F 18 D0 0E 01  ot0...y.........
0480: 1C 07 80 5B 20 80 2B D0  0E 01 2B D0 0E 01 77 72  ...[ .+...+...wr
0490: 61 30 1C 0C 80 45 0B 80  F0 FF FF 7F F0 FF FF 7F  a0...E..........
04A0: 6F 76 6C 32 06 80 55 0E  80 F0 FF FF 7F F0 FF FF  ovl2..U.........
04B0: 7F 73 30 37 31 45 0E 80  F0 FF FF 7F F0 FF FF 7F  .s071E..........
04C0: 73 30 37 32 06 80 1C 2D  80 5D 06 80 0C 80 45 0B  s072...-.]....E.
04D0: 80 F0 FF FF 7F F0 FF FF  7F 66 64 6F 32 06 80 1C  .........fdo2...
04E0: 0C 80 5C 00 2E 80 5C 01  2E 80 55 0E 80 F0 FF FF  ..\...\...U.....
04F0: 7F F0 FF FF 7F 73 30 37  32 46 00 45 0B 80 F0 FF  .....s072F.E....
0500: FF 7F F0 FF FF 7F 66 64  69 32 06 80 45 2F 80 F8  ......fdi2..E/..
0510: FF FF 7F F8 FF FF 7F 71  73 74 63 06 80 21 00     .......qstc..!. 
```

#### Opcodes

```
  0: 0x009D [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x009E [0x75] LOAD_ROOM(Load indoor room, room=303*)
  2: 0x00A2 [0x75] LOAD_ROOM(No action)
  3: 0x00A4 [0x4C] EventEntity->StatusEvent = 8 // Open door
  4: 0x00A5 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=60*)
  5: 0x00AA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
  6: 0x00BB [0x1C] WAIT(60* ticks)
  7: 0x00BE [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 120*
  8: 0x00C2 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 120*
  9: 0x00C6 [0x46] CAMERA_CONTROL: Disable user control
 10: 0x00C8 [0x38] SET_CLIENT_EVENT_MODE(mode=3*)
 11: 0x00CB [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x17)
 12: 0x00D2 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s066" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 13: 0x00E3 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi1" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 14: 0x00F4 [0x4A] Volker (ID: 17748014/0x010ED02E) looks at LocalPlayer
 15: 0x00FD [0x1C] WAIT(60* ticks)
 16: 0x0100 [0x1C] WAIT(120* ticks)
 17: 0x0103 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlb0" with entities [Volker (ID: 17748014/0x010ED02E), Volker (ID: 17748014/0x010ED02E)], work=200*
 18: 0x0112 [0x79] LocalPlayer looks at Volker (ID: 17748014/0x010ED02E) (Basic look)
 19: 0x011C [0x2B] Volker (ID: 17748014/0x010ED02E) [7943*]:
    → "You've done it! You stopped them from bringing back the Shadow Lord!?"
 20: 0x0123 [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x0124 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ev00" with entities [Volker (ID: 17748014/0x010ED02E), Volker (ID: 17748014/0x010ED02E)], work=200*
 22: 0x0133 [0x27] REQ_SET(priority=0x0A, entity_id=Cid (ID: 17748011/0x010ED02B), tag_num=0x11)
 23: 0x013A [0x79] LocalPlayer looks at Cid (ID: 17748011/0x010ED02B) (Basic look)
 24: 0x0144 [0x2B] Cid (ID: 17748011/0x010ED02B) [7944*]:
    → "What are you talking about, Volker? They probably defeated him and sent him back where he belongs! Am I right?"
 25: 0x014B [0x23] WAIT_FOR_DIALOG_INTERACTION
 26: 0x014C [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "ib01" with entities [Volker (ID: 17748014/0x010ED02E), Volker (ID: 17748014/0x010ED02E)], work=200*
 27: 0x015B [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s066" with entities [LocalPlayer, LocalPlayer], work=137*
 28: 0x016A [0x2B] Volker (ID: 17748014/0x010ED02E) [7945*]:
    → "What? Defeat him? But that's..."
 29: 0x0171 [0x23] WAIT_FOR_DIALOG_INTERACTION
 30: 0x0172 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cid (ID: 17748011/0x010ED02B))
 31: 0x0178 [0x27] REQ_SET(priority=0x0A, entity_id=Lucius (ID: 17747992/0x010ED018), tag_num=0x17)
 32: 0x017F [0x1C] WAIT(30* ticks)
 33: 0x0182 [0x79] LocalPlayer looks at Lucius (ID: 17747992/0x010ED018) (Basic look)
 34: 0x018C [0x79] Cid (ID: 17748011/0x010ED02B) looks at Lucius (ID: 17747992/0x010ED018) (Basic look)
 35: 0x0196 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s067" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 36: 0x01A7 [0x2B] Lucius (ID: 17747992/0x010ED018) [7946*]:
    → "Impossible? You find it hard to believe that some adventurer could defeat the Shadow Lord, Captain? Have you not heard what the townspeople are saying?"
 37: 0x01AE [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x01AF [0x4A] Cid (ID: 17748011/0x010ED02B) looks at Volker (ID: 17748014/0x010ED02E)
 39: 0x01B8 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
 40: 0x01B9 [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until Cid (ID: 17748011/0x010ED02B) Render.Flags0 and Render.Flags3 conditions are met
 41: 0x01BE [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=110*
 42: 0x01CD [0x2B] Cid (ID: 17748011/0x010ED02B) [7947*]:
    → "They're saying the Age of the Adventurers has come!"
 43: 0x01D4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 44: 0x01D5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=110*
 45: 0x01E4 [0x27] REQ_SET(priority=0x0A, entity_id=Karst (ID: 17748010/0x010ED02A), tag_num=0x15)
 46: 0x01EB [0x1C] WAIT(30* ticks)
 47: 0x01EE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s068" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 48: 0x01FF [0x2B] Karst (ID: 17748010/0x010ED02A) [7948*]:
    → "Hmph. Only historians, in posterity, have the privilege of saying such things."
 49: 0x0206 [0x23] WAIT_FOR_DIALOG_INTERACTION
 50: 0x0207 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Karst (ID: 17748010/0x010ED02A))
 51: 0x020D [0x79] Karst (ID: 17748010/0x010ED02A) looks at LocalPlayer (Basic look)
 52: 0x0217 [0x2B] Karst (ID: 17748010/0x010ED02A) [7949*]:
    → "And it does not matter if they only stopped the Shadow Lord from returning, or if they actually defeated him."
 53: 0x021E [0x23] WAIT_FOR_DIALOG_INTERACTION
 54: 0x021F [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Karst (ID: 17748010/0x010ED02A), Karst (ID: 17748010/0x010ED02A)], work=150*
 55: 0x022E [0x2B] Karst (ID: 17748010/0x010ED02A) [7950*]:
    → "The important thing is that they kept the Kindred from gaining power. And that, I believe, deserves a reward."
 56: 0x0235 [0x23] WAIT_FOR_DIALOG_INTERACTION
 57: 0x0236 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Karst (ID: 17748010/0x010ED02A), Karst (ID: 17748010/0x010ED02A)], work=150*
 58: 0x0245 [0x2B] Karst (ID: 17748010/0x010ED02A) [7951*]:
    → "Good work. I am raising your rank. And here is your well-deserved reward."
 59: 0x024C [0x23] WAIT_FOR_DIALOG_INTERACTION
 60: 0x024D [0x79] Cid (ID: 17748011/0x010ED02B) looks at LocalPlayer (Basic look)
 61: 0x0257 [0x27] REQ_SET(priority=0x0A, entity_id=Lucius (ID: 17747992/0x010ED018), tag_num=0x18)
 62: 0x025E [0x1C] WAIT(20* ticks)
 63: 0x0261 [0x2B] Lucius (ID: 17747992/0x010ED018) [7952*]:
    → "The Shadow Lord may have been vanquished again, but the Kindred are far from defeated. I have received reports of strange goings-on in the beastmen's strongholds."
 64: 0x0268 [0x23] WAIT_FOR_DIALOG_INTERACTION
 65: 0x0269 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=110*
 66: 0x0278 [0x2B] Cid (ID: 17748011/0x010ED02B) [7953*]:
    → "You've probably heard this too many times, but...we're counting on you."
 67: 0x027F [0x23] WAIT_FOR_DIALOG_INTERACTION
 68: 0x0280 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=110*
 69: 0x028F [0x7D] LOAD_START_SCHEDULER_PLAYER: Load scheduler with animation_id 32797
 70: 0x0292 [0x1C] WAIT(120* ticks)
 71: 0x0295 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 72: 0x02A6 [0x1C] WAIT(120* ticks)
 73: 0x02A9 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s069" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 74: 0x02BA [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
 75: 0x02CB [0x4D] EventEntity->StatusEvent = 9 // Close door
 76: 0x02CC [0x27] REQ_SET(priority=0x0A, entity_id=LocalPlayer, tag_num=0x19)
 77: 0x02D3 [0x27] REQ_SET(priority=0x0A, entity_id=Cid (ID: 17748011/0x010ED02B), tag_num=0x12)
 78: 0x02DA [0x1C] WAIT(120* ticks)
 79: 0x02DD [0x2B] Cid (ID: 17748011/0x010ED02B) [7954*]:
    → "So that was who the Shadow Lord was... Zeid must have known, and that's probably why he went off on his own."
 80: 0x02E4 [0x23] WAIT_FOR_DIALOG_INTERACTION
 81: 0x02E5 [0x2A] GET_REQ_LEVEL(level=10, entity_id=Cid (ID: 17748011/0x010ED02B))
 82: 0x02EB [0x4A] Cid (ID: 17748011/0x010ED02B) looks at LocalPlayer
 83: 0x02F4 [0x79] LocalPlayer looks at Cid (ID: 17748011/0x010ED02B) (Basic look)
 84: 0x02FE [0x2B] Cid (ID: 17748011/0x010ED02B) [7955*]:
    → "Don't tell Volker about this. Ulrich's fate should also be kept from him, too. He may not be able to accept it yet."
 85: 0x0305 [0x23] WAIT_FOR_DIALOG_INTERACTION
 86: 0x0306 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk0" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=111*
 87: 0x0315 [0x2B] Cid (ID: 17748011/0x010ED02B) [7956*]:
    → "He admired his grandfather a lot...that's why it pained him to hear people say that Volker, himself, only became Captain because Raogrimm was gone."
 88: 0x031C [0x23] WAIT_FOR_DIALOG_INTERACTION
 89: 0x031D [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s069" with entities [LocalPlayer, LocalPlayer], work=137*
 90: 0x032C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s070" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
 91: 0x033D [0x2B] Cid (ID: 17748011/0x010ED02B) [7957*]:
    → "I know that hiding the truth from him is not a good thing, but most of us are not as strong as you. We need time to heal."
 92: 0x0344 [0x23] WAIT_FOR_DIALOG_INTERACTION
 93: 0x0345 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tlk1" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=111*
 94: 0x0354 [0x27] REQ_SET(priority=0x0A, entity_id=Lucius (ID: 17747992/0x010ED018), tag_num=0x19)
 95: 0x035B [0x1C] WAIT(120* ticks)
 96: 0x035E [0x2B] Lucius (ID: 17747992/0x010ED018) [7958*]:
    → "Sorry to interrupt. What are you two talking about?"
 97: 0x0365 [0x23] WAIT_FOR_DIALOG_INTERACTION
 98: 0x0366 [0x27] REQ_SET(priority=0x0A, entity_id=Volker (ID: 17748014/0x010ED02E), tag_num=0x19)
 99: 0x036D [0x4A] Cid (ID: 17748011/0x010ED02B) looks at Lucius (ID: 17747992/0x010ED018)
100: 0x0376 [0x2B] Cid (ID: 17748011/0x010ED02B) [7959*]:
    → "Uh...just saying that Karst really hasn't changed, even after all of this."
101: 0x037D [0x23] WAIT_FOR_DIALOG_INTERACTION
102: 0x037E [0x2A] GET_REQ_LEVEL(level=10, entity_id=Volker (ID: 17748014/0x010ED02E))
103: 0x0384 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla0" with entities [Volker (ID: 17748014/0x010ED02E), Volker (ID: 17748014/0x010ED02E)], work=200*
104: 0x0393 [0x79] Cid (ID: 17748011/0x010ED02B) looks at Volker (ID: 17748014/0x010ED02E) (Basic look)
105: 0x039D [0x2B] Volker (ID: 17748014/0x010ED02E) [7960*]:
    → "Yes, but I think I understand him better now. I may have been judging him too harshly."
106: 0x03A4 [0x23] WAIT_FOR_DIALOG_INTERACTION
107: 0x03A5 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "tla1" with entities [Volker (ID: 17748014/0x010ED02E), Volker (ID: 17748014/0x010ED02E)], work=200*
108: 0x03B4 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [Lucius (ID: 17747992/0x010ED018), Lucius (ID: 17747992/0x010ED018)], work=0*
109: 0x03C3 [0x2B] Lucius (ID: 17747992/0x010ED018) [7961*]:
    → "Speaking of which...you still have not told us why you backed President Karst in the last elections, Chief."
110: 0x03CA [0x23] WAIT_FOR_DIALOG_INTERACTION
111: 0x03CB [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "ten0" with entities [Lucius (ID: 17747992/0x010ED018), Lucius (ID: 17747992/0x010ED018)], work=0*
112: 0x03DA [0x7B] Cid (ID: 17748011/0x010ED02B) stops talking
113: 0x03DF [0x4B] UPDATE_ENTITY_YAW(entity=Cid (ID: 17748011/0x010ED02B), yaw=11.2°*)
114: 0x03E6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s070" with entities [LocalPlayer, LocalPlayer], work=137*
115: 0x03F5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s071" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
116: 0x0406 [0x1C] WAIT(30* ticks)
117: 0x0409 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "omo0" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=111*
118: 0x0418 [0x2B] Cid (ID: 17748011/0x010ED02B) [7962*]:
    → "Oh, that. Well... Fifteen years ago, even after I resigned my post as head of the Gunpowder Room, the Senate was still in chaos, trying to find more people to blame for the accident in Palborough."
119: 0x041F [0x23] WAIT_FOR_DIALOG_INTERACTION
120: 0x0420 [0x2B] Cid (ID: 17748011/0x010ED02B) [7963*]:
    → "But there was one junior senator there who proposed we abandon Palborough and reopen the Zeruhn Mines. That junior senator was Karst."
121: 0x0427 [0x23] WAIT_FOR_DIALOG_INTERACTION
122: 0x0428 [0x2B] Cid (ID: 17748011/0x010ED02B) [7964*]:
    → "The miners stood to lose a lot, but at the time, his proposal was Bastok's best bet. I'm an engineer, so I respect skill. And I felt that Karst's political skills could be trusted."
123: 0x042F [0x23] WAIT_FOR_DIALOG_INTERACTION
124: 0x0430 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "omo1" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=111*
125: 0x043F [0x2B] Cid (ID: 17748011/0x010ED02B) [7965*]:
    → "And he's a real Bastoker, too--very ambitious, and real easy to figure out. I can still remember the eager look on his face when he announced his proposal to the Senate!"
126: 0x0446 [0x23] WAIT_FOR_DIALOG_INTERACTION
127: 0x0447 [0x1C] WAIT(10* ticks)
128: 0x044A [0x79] Volker (ID: 17748014/0x010ED02E) looks at Lucius (ID: 17747992/0x010ED018) (Basic look)
129: 0x0454 [0x1C] WAIT(30* ticks)
130: 0x0457 [0x79] Lucius (ID: 17747992/0x010ED018) looks at Volker (ID: 17748014/0x010ED02E) (Basic look)
131: 0x0461 [0x1C] WAIT(20* ticks)
132: 0x0464 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "not0" with entities [Volker (ID: 17748014/0x010ED02E), Volker (ID: 17748014/0x010ED02E)], work=200*
133: 0x0473 [0x1C] WAIT(20* ticks)
134: 0x0476 [0x79] LocalPlayer looks at Lucius (ID: 17747992/0x010ED018) (Basic look)
135: 0x0480 [0x1C] WAIT(30* ticks)
136: 0x0483 [0x5B] LOAD_EXT_SCHEDULER: Load scheduler "wra0" with entities [Cid (ID: 17748011/0x010ED02B), Cid (ID: 17748011/0x010ED02B)], work=111*
137: 0x0492 [0x1C] WAIT(120* ticks)
138: 0x0495 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "ovl2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
139: 0x04A6 [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s071" with entities [LocalPlayer, LocalPlayer], work=137*
140: 0x04B5 [0x45] LOAD_SCHEDULED_TASK: Load scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=[137*, 0*]
141: 0x04C6 [0x1C] WAIT(240* ticks)
142: 0x04C9 [0x5D] SET_MUSIC_VOLUME(volume=0*, fade_time=120*)
143: 0x04CE [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdo2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
144: 0x04DF [0x1C] WAIT(120* ticks)
145: 0x04E2 [0x5C] MUSIC_CONTROL: Set Idle (Day) music to song 154*
146: 0x04E6 [0x5C] MUSIC_CONTROL: Set Idle (Night) music to song 154*
147: 0x04EA [0x55] WAIT_LOAD_SCHEDULER: Wait for scheduler "s072" with entities [LocalPlayer, LocalPlayer], work=137*
148: 0x04F9 [0x46] CAMERA_CONTROL: Restore default settings
149: 0x04FB [0x45] LOAD_SCHEDULED_TASK: Load scheduler "fdi2" with entities [LocalPlayer, LocalPlayer], work=[200*, 0*]
150: 0x050C [0x45] LOAD_SCHEDULED_TASK: Load scheduler "qstc" with entities [EventEntity, EventEntity], work=[201*, 0*]
151: 0x051D [0x21] END_EVENT
152: 0x051E [0x00] END_REQSTACK()
```

### Event 780

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x051F  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0510:                                               00                 .
```

#### Opcodes

```
  0: 0x051F [0x00] END_REQSTACK()
```

### Event 782

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0520  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0520: 00                                                .               
```

#### Opcodes

```
  0: 0x0520 [0x00] END_REQSTACK()
```

### Event 829

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0521  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0520:    00                                              .              
```

#### Opcodes

```
  0: 0x0521 [0x00] END_REQSTACK()
```

### Event 968

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0522  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0520:       00                                            .             
```

#### Opcodes

```
  0: 0x0522 [0x00] END_REQSTACK()
```

### Event 1051

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0523  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0520:          4D 00                                       M.           
```

#### Opcodes

```
  0: 0x0523 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0524 [0x00] END_REQSTACK()
```

### Event 1052

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0525  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0520:                4D 00                                   M.         
```

#### Opcodes

```
  0: 0x0525 [0x4D] EventEntity->StatusEvent = 9 // Close door
  1: 0x0526 [0x00] END_REQSTACK()
```
