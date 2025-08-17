# 17580385 - Strange Apparatus

## Common Data

| Field            | Value                  |
|------------------|------------------------|
| Zone             | Gusgen Mines (ID: 196) |
| Block Size       | 600 bytes              |
| Total Events     | 4                      |
| References Count | 40                     |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [0](#event-0)         | 0x0001       |    204 |             69 |
| [2](#event-2)         | 0x00CD       |    200 |             45 |
| [1](#event-1)         | 0x0195       |      2 |              2 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1C9F      |        7327 |
|       1 | 0x00BF      |         191 |
|       2 | 0x1CA0      |        7328 |
|       3 | 0x00C5      |         197 |
|       4 | 0x1CA1      |        7329 |
|       5 | 0x00C4      |         196 |
|       6 | 0x1CA2      |        7330 |
|       7 | 0x00C1      |         193 |
|       8 | 0x1CA3      |        7331 |
|       9 | 0x00C3      |         195 |
|      10 | 0x1CA4      |        7332 |
|      11 | 0x00C2      |         194 |
|      12 | 0x1CA5      |        7333 |
|      13 | 0x00C8      |         200 |
|      14 | 0x1CA6      |        7334 |
|      15 | 0x00C6      |         198 |
|      16 | 0x1CA7      |        7335 |
|      17 | 0x1CB9      |        7353 |
|      18 | 0x1CA8      |        7336 |
|      19 | 0x0000      |           0 |
|      20 | 0x1CAE      |        7342 |
|      21 | 0x1CAF      |        7343 |
|      22 | 0x1CB0      |        7344 |
|      23 | 0x1CB1      |        7345 |
|      24 | 0x1CB3      |        7347 |
|      25 | 0x1CB2      |        7346 |
|      26 | 0x1CA9      |        7337 |
|      27 | 0x1CAB      |        7339 |
|      28 | 0x1CBA      |        7354 |
|      29 | 0x1CB5      |        7349 |
|      30 | 0x00B4      |         180 |
|      31 | 0x1000      |        4096 |
|      32 | 0x1007      |        4103 |
|      33 | 0x00F0      |         240 |
|      34 | 0x012C      |         300 |
|      35 | 0x0001      |           1 |
|      36 | 0x1CAC      |        7340 |
|      37 | 0x1CBC      |        7356 |
|      38 | 0x1CB4      |        7348 |
|      39 | 0x1CAA      |        7338 |

## String References

- **7327**: It is some sort of device.
- **7328**: You can feel hot steam leaking from the cracks in the machine...
- **7329**: It feels a little damp...
- **7330**: It looks a little dusty...
- **7331**: You can feel a little air leaking from the cracks in the machine...
- **7332**: You can feel a stream of cold air leaking from the cracks in the machine...
- **7333**: You can hear a small crackling sound from the inside...
- **7334**: You start to feel a little lightheaded...
- **7335**: You start to feel a little dark and gloomy...
- **7336**: The voice of a young woman rings in your head.
- **7337**: "...thorization...grant... ...lcome...octor <Player>..."
- **7338**: "It is...will...Altan... ...heaven...lory...ve...mercy..."
- **7339**: The voice in your head has gone silent.
- **7340**: You obtain $0!
- **7342**: "Wel...to the...morph Matter Emulato... Inser...$2 and...elementally c...patible chip to begi...item replicat...process..."
- **7343**: "If you...a registe...doctor, emula...ettings will...djuste...accordin..."
- **7344**: "...emulator...ill now conduc...user auth...zation. Please inp...your 8-digit passw..."
- **7345**: "Registr...n complete. Your access...evel is doctor."
- **7346**: "Passw...error... Reg...tration comple... Your access lev...is assistant."
- **7347**: "Yo...dat...has be...recorde..."
- **7348**: "Syste...shutting...own."
- **7349**: "...commencin...rocess..."
- **7353**: There is no response...
- **7354**: "S-level warni... Shutti...own systems...prevent...stem overlo..."
- **7356**: You obtain $1 $0 .

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

### Event 0

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 204 bytes |
| Instructions | 69        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    48 00 80 23 02 09 10  01 80 80 14 00 48 02 80   H..#........H..
0010: 23 01 83 00 02 09 10 03  80 80 23 00 48 04 80 23  #.........#.H..#
0020: 01 83 00 02 09 10 05 80  80 32 00 48 06 80 23 01  .........2.H..#.
0030: 83 00 02 09 10 07 80 80  41 00 48 08 80 23 01 83  ........A.H..#..
0040: 00 02 09 10 09 80 80 50  00 48 0A 80 23 01 83 00  .......P.H..#...
0050: 02 09 10 0B 80 80 5F 00  48 0C 80 23 01 83 00 02  ......_.H..#....
0060: 09 10 0D 80 80 6E 00 48  0E 80 23 01 83 00 02 09  .....n.H..#.....
0070: 10 0F 80 80 7D 00 48 10  80 23 01 83 00 48 11 80  ....}.H..#...H..
0080: 23 21 00 48 12 80 23 02  02 10 13 80 00 BB 00 48  #!.H..#........H
0090: 14 80 23 48 15 80 23 48  16 80 23 71 00 71 01 71  ..#H..#H..#q.q.q
00A0: 02 02 02 10 13 80 00 B4  00 48 17 80 23 48 18 80  .........H..#H..
00B0: 23 01 B8 00 48 19 80 23  01 C7 00 48 1A 80 23 48  #...H..#...H..#H
00C0: 14 80 23 48 15 80 23 48  1B 80 23 21 00           ..#H..#H..#!.   
```

#### Opcodes

```
  0: 0x0001 [0x48] [System] [7327*]:
    → "It is some sort of device."
  1: 0x0004 [0x23] WAIT_FOR_DIALOG_INTERACTION
  2: 0x0005 [0x02] IF !(Work_Zone[9] == 191*) GOTO 0x0014
  3: 0x000D [0x48] [System] [7328*]:
    → "You can feel hot steam leaking from the cracks in the machine..."
  4: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x0011 [0x01] GOTO 0x0083
  6: 0x0014 [0x02] IF !(Work_Zone[9] == 197*) GOTO 0x0023
  7: 0x001C [0x48] [System] [7329*]:
    → "It feels a little damp..."
  8: 0x001F [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0020 [0x01] GOTO 0x0083
 10: 0x0023 [0x02] IF !(Work_Zone[9] == 196*) GOTO 0x0032
 11: 0x002B [0x48] [System] [7330*]:
    → "It looks a little dusty..."
 12: 0x002E [0x23] WAIT_FOR_DIALOG_INTERACTION
 13: 0x002F [0x01] GOTO 0x0083
 14: 0x0032 [0x02] IF !(Work_Zone[9] == 193*) GOTO 0x0041
 15: 0x003A [0x48] [System] [7331*]:
    → "You can feel a little air leaking from the cracks in the machine..."
 16: 0x003D [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x003E [0x01] GOTO 0x0083
 18: 0x0041 [0x02] IF !(Work_Zone[9] == 195*) GOTO 0x0050
 19: 0x0049 [0x48] [System] [7332*]:
    → "You can feel a stream of cold air leaking from the cracks in the machine..."
 20: 0x004C [0x23] WAIT_FOR_DIALOG_INTERACTION
 21: 0x004D [0x01] GOTO 0x0083
 22: 0x0050 [0x02] IF !(Work_Zone[9] == 194*) GOTO 0x005F
 23: 0x0058 [0x48] [System] [7333*]:
    → "You can hear a small crackling sound from the inside..."
 24: 0x005B [0x23] WAIT_FOR_DIALOG_INTERACTION
 25: 0x005C [0x01] GOTO 0x0083
 26: 0x005F [0x02] IF !(Work_Zone[9] == 200*) GOTO 0x006E
 27: 0x0067 [0x48] [System] [7334*]:
    → "You start to feel a little lightheaded..."
 28: 0x006A [0x23] WAIT_FOR_DIALOG_INTERACTION
 29: 0x006B [0x01] GOTO 0x0083
 30: 0x006E [0x02] IF !(Work_Zone[9] == 198*) GOTO 0x007D
 31: 0x0076 [0x48] [System] [7335*]:
    → "You start to feel a little dark and gloomy..."
 32: 0x0079 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x007A [0x01] GOTO 0x0083
 34: 0x007D [0x48] [System] [7353*]:
    → "There is no response..."
 35: 0x0080 [0x23] WAIT_FOR_DIALOG_INTERACTION
 36: 0x0081 [0x21] END_EVENT
 37: 0x0082 [0x00] END_REQSTACK()

SUBROUTINE_0083:
 38: 0x0083 [0x48] [System] [7336*]:
    → "The voice of a young woman rings in your head."
 39: 0x0086 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x0087 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00BB
 41: 0x008F [0x48] [System] [7342*]:
    → ""Wel...to the...morph Matter Emulato... Inser...$2 and...elementally c...patible chip to begi...item replicat...process...""
 42: 0x0092 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x0093 [0x48] [System] [7343*]:
    → ""If you...a registe...doctor, emula...ettings will...djuste...accordin...""
 44: 0x0096 [0x23] WAIT_FOR_DIALOG_INTERACTION
 45: 0x0097 [0x48] [System] [7344*]:
    → ""...emulator...ill now conduc...user auth...zation. Please inp...your 8-digit passw...""
 46: 0x009A [0x23] WAIT_FOR_DIALOG_INTERACTION
 47: 0x009B [0x71] USER_INPUT_HANDLER: Open password input dialog (sends packet 0x60)
 48: 0x009D [0x71] USER_INPUT_HANDLER: Check if player has input or exited
 49: 0x009F [0x71] USER_INPUT_HANDLER: Check if server responded
 50: 0x00A1 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x00B4
 51: 0x00A9 [0x48] [System] [7345*]:
    → ""Registr...n complete. Your access...evel is doctor.""
 52: 0x00AC [0x23] WAIT_FOR_DIALOG_INTERACTION
 53: 0x00AD [0x48] [System] [7347*]:
    → ""Yo...dat...has be...recorde...""
 54: 0x00B0 [0x23] WAIT_FOR_DIALOG_INTERACTION
 55: 0x00B1 [0x01] GOTO 0x00B8
 56: 0x00B4 [0x48] [System] [7346*]:
    → ""Passw...error... Reg...tration comple... Your access lev...is assistant.""
 57: 0x00B7 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00B8:
 58: 0x00B8 [0x01] GOTO 0x00C7
 59: 0x00BB [0x48] [System] [7337*]:
    → ""...thorization...grant... ...lcome...octor <Player>...""
 60: 0x00BE [0x23] WAIT_FOR_DIALOG_INTERACTION
 61: 0x00BF [0x48] [System] [7342*]:
    → ""Wel...to the...morph Matter Emulato... Inser...$2 and...elementally c...patible chip to begi...item replicat...process...""
 62: 0x00C2 [0x23] WAIT_FOR_DIALOG_INTERACTION
 63: 0x00C3 [0x48] [System] [7343*]:
    → ""If you...a registe...doctor, emula...ettings will...djuste...accordin...""
 64: 0x00C6 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_00C7:
 65: 0x00C7 [0x48] [System] [7339*]:
    → "The voice in your head has gone silent."
 66: 0x00CA [0x23] WAIT_FOR_DIALOG_INTERACTION
 67: 0x00CB [0x21] END_EVENT
 68: 0x00CC [0x00] END_REQSTACK()
```

### Event 2

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x00CD    |
| Data Size    | 200 bytes |
| Instructions | 45        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
00C0:                                         20 01 42                .B
00D0: 4A F0 FF FF 7F F8 FF FF  7F 48 12 80 23 02 09 10  J........H..#...
00E0: 13 80 01 EF 00 48 1C 80  23 48 1B 80 23 21 00 2D  .....H..#H..#!.-
00F0: 61 41 0C 01 61 41 0C 01  6D 6E 74 72 2D 61 41 0C  aA..aA..mntr-aA.
0100: 01 61 41 0C 01 6D 6F 6A  69 02 08 10 13 80 01 15  .aA..moji.......
0110: 01 48 1A 80 23 48 1D 80  23 2D 61 41 0C 01 61 41  .H..#H..#-aA..aA
0120: 0C 01 69 74 69 6E 1C 1E  80 06 00 00 02 02 10 1F  ..itin..........
0130: 80 04 4F 01 02 02 10 20  80 05 4F 01 05 00 00 2D  ..O.... ..O....-
0140: 61 41 0C 01 61 41 0C 01  63 72 6F 74 1C 21 80 02  aA..aA..crot.!..
0150: 00 00 13 80 00 67 01 2D  61 41 0C 01 61 41 0C 01  .....g.-aA..aA..
0160: 69 74 6F 74 1C 22 80 02  03 10 23 80 00 76 01 48  itot."....#..v.H
0170: 24 80 23 01 7A 01 48 25  80 23 48 26 80 23 48 27  $.#.z.H%.#H&.#H'
0180: 80 23 2D 61 41 0C 01 61  41 0C 01 6B 69 6C 6C 48  .#-aA..aA..killH
0190: 1B 80 23 21 00                                    ..#!.           
```

#### Opcodes

```
  0: 0x00CD [0x20] SET_CLI_EVENT_UC_FLAG: Lock player control
  1: 0x00CF [0x42] SET_CLI_EVENT_CANCEL_DATA()
  2: 0x00D0 [0x4A] LocalPlayer looks at EventEntity
  3: 0x00D9 [0x48] [System] [7336*]:
    → "The voice of a young woman rings in your head."
  4: 0x00DC [0x23] WAIT_FOR_DIALOG_INTERACTION
  5: 0x00DD [0x02] IF !(Work_Zone[9] == 0*) GOTO 0x00EF
  6: 0x00E5 [0x48] [System] [7354*]:
    → ""S-level warni... Shutti...own systems...prevent...stem overlo...""
  7: 0x00E8 [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x00E9 [0x48] [System] [7339*]:
    → "The voice in your head has gone silent."
  9: 0x00EC [0x23] WAIT_FOR_DIALOG_INTERACTION
 10: 0x00ED [0x21] END_EVENT
 11: 0x00EE [0x00] END_REQSTACK()
 12: 0x00EF [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "mntr" with entities [Strange Apparatus (ID: 17580385/0x010C4161), Strange Apparatus (ID: 17580385/0x010C4161)]
 13: 0x00FC [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "moji" with entities [Strange Apparatus (ID: 17580385/0x010C4161), Strange Apparatus (ID: 17580385/0x010C4161)]
 14: 0x0109 [0x02] IF !(Work_Zone[8] == 0*) GOTO 0x0115
 15: 0x0111 [0x48] [System] [7337*]:
    → ""...thorization...grant... ...lcome...octor <Player>...""
 16: 0x0114 [0x23] WAIT_FOR_DIALOG_INTERACTION
 17: 0x0115 [0x48] [System] [7349*]:
    → ""...commencin...rocess...""
 18: 0x0118 [0x23] WAIT_FOR_DIALOG_INTERACTION
 19: 0x0119 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "itin" with entities [Strange Apparatus (ID: 17580385/0x010C4161), Strange Apparatus (ID: 17580385/0x010C4161)]
 20: 0x0126 [0x1C] WAIT(180* ticks)
 21: 0x0129 [0x06] ExtData[1]->WorkLocal[0] = 0
 22: 0x012C [0x02] IF !(Work_Zone[2] < 4096*) GOTO 0x014F
 23: 0x0134 [0x02] IF !(Work_Zone[2] > 4103*) GOTO 0x014F
 24: 0x013C [0x05] ExtData[1]->WorkLocal[0] = 1
 25: 0x013F [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "crot" with entities [Strange Apparatus (ID: 17580385/0x010C4161), Strange Apparatus (ID: 17580385/0x010C4161)]
 26: 0x014C [0x1C] WAIT(240* ticks)
 27: 0x014F [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0167
 28: 0x0157 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "itot" with entities [Strange Apparatus (ID: 17580385/0x010C4161), Strange Apparatus (ID: 17580385/0x010C4161)]
 29: 0x0164 [0x1C] WAIT(300* ticks)
 30: 0x0167 [0x02] IF !(Work_Zone[3] == 1*) GOTO 0x0176
 31: 0x016F [0x48] [System] [7340*]:
    → "You obtain $0!"
 32: 0x0172 [0x23] WAIT_FOR_DIALOG_INTERACTION
 33: 0x0173 [0x01] GOTO 0x017A
 34: 0x0176 [0x48] [System] [7356*]:
    → "You obtain $1 $0 ."
 35: 0x0179 [0x23] WAIT_FOR_DIALOG_INTERACTION

SUBROUTINE_017A:
 36: 0x017A [0x48] [System] [7348*]:
    → ""Syste...shutting...own.""
 37: 0x017D [0x23] WAIT_FOR_DIALOG_INTERACTION
 38: 0x017E [0x48] [System] [7338*]:
    → ""It is...will...Altan... ...heaven...lory...ve...mercy...""
 39: 0x0181 [0x23] WAIT_FOR_DIALOG_INTERACTION
 40: 0x0182 [0x2D] CREATE_ZONE_SCHEDULER_TASK: Create scheduler "kill" with entities [Strange Apparatus (ID: 17580385/0x010C4161), Strange Apparatus (ID: 17580385/0x010C4161)]
 41: 0x018F [0x48] [System] [7339*]:
    → "The voice in your head has gone silent."
 42: 0x0192 [0x23] WAIT_FOR_DIALOG_INTERACTION
 43: 0x0193 [0x21] END_EVENT
 44: 0x0194 [0x00] END_REQSTACK()
```

### Event 1

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0195  |
| Data Size    | 2 bytes |
| Instructions | 2       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0190:                21 00                                   !.         
```

#### Opcodes

```
  0: 0x0195 [0x21] END_EVENT
  1: 0x0196 [0x00] END_REQSTACK()
```
