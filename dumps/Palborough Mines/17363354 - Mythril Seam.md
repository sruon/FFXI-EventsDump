# 17363354 - Mythril Seam

## Common Data

| Field            | Value                      |
|------------------|----------------------------|
| Zone             | Palborough Mines (ID: 143) |
| Block Size       | 240 bytes                  |
| Total Events     | 5                          |
| References Count | 14                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [54](#event-54)       | 0x0001       |     15 |              5 |
| [56](#event-56)       | 0x0010       |     15 |              5 |
| [55](#event-55)       | 0x001F       |     96 |             22 |
| [57](#event-57)       | 0x007F       |     18 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x1CC3      |        7363 |
|       1 | 0x1CC6      |        7366 |
|       2 | 0x0029      |          41 |
|       3 | 0x0000      |           0 |
|       4 | 0x1CCD      |        7373 |
|       5 | 0x0004      |           4 |
|       6 | 0x0255      |         597 |
|       7 | 0x1CF9      |        7417 |
|       8 | 0x0008      |           8 |
|       9 | 0x025D      |         605 |
|      10 | 0x1CCC      |        7372 |
|      11 | 0x000C      |          12 |
|      12 | 0x1CCB      |        7371 |
|      13 | 0x1CFC      |        7420 |

## String References

- **7363**: You should be able to mine mythril here.
- **7366**: You will need a proper tool to dig here.
- **7371**: You find $1, but your $2 breaks in the process.
- **7372**: Your $1 breaks!
- **7373**: You find nothing.
- **7417**: You successfully dig up $0!
- **7420**: You cannot carry any more items. Your inventory is full.

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

### Event 54

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    4A F0 FF FF 7F 9A F1  08 01 48 00 80 23 21 00   J........H..#!.
```

#### Opcodes

```
  0: 0x0001 [0x4A] LocalPlayer looks at Mythril Seam (ID: 17363354/0x0108F19A)
  1: 0x000A [0x48] [System] [7363*]:
    → "You should be able to mine mythril here."
  2: 0x000D [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x000E [0x21] END_EVENT
  4: 0x000F [0x00] END_REQSTACK()
```

### Event 56

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0010   |
| Data Size    | 15 bytes |
| Instructions | 5        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010: 4A F0 FF FF 7F 9A F1 08  01 48 01 80 23 21 00     J........H..#!. 
```

#### Opcodes

```
  0: 0x0010 [0x4A] LocalPlayer looks at Mythril Seam (ID: 17363354/0x0108F19A)
  1: 0x0019 [0x48] [System] [7366*]:
    → "You will need a proper tool to dig here."
  2: 0x001C [0x23] WAIT_FOR_DIALOG_INTERACTION
  3: 0x001D [0x21] END_EVENT
  4: 0x001E [0x00] END_REQSTACK()
```

### Event 55

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x001F   |
| Data Size    | 96 bytes |
| Instructions | 22       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                                               42                 B
0020: 6E F0 FF FF 7F 02 80 99  F0 FF FF 7F 03 00 00 02  n...............
0030: 10 02 00 00 03 80 80 3F  00 48 04 80 01 7D 00 02  .......?.H...}..
0040: 00 00 05 80 80 52 00 03  02 10 06 80 48 07 80 01  .....R......H...
0050: 7D 00 02 00 00 08 80 80  65 00 03 03 10 09 80 48  }.......e......H
0060: 0A 80 01 7D 00 02 00 00  0B 80 80 7D 00 03 03 10  ...}.......}....
0070: 06 80 03 04 10 09 80 48  0C 80 01 7D 00 21 00     .......H...}.!. 
```

#### Opcodes

```
  0: 0x001F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0020 [0x6E] LocalPlayer uses emote 41*
  2: 0x0027 [0x99] Wait for LocalPlayer animation to complete
  3: 0x002C [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[2]
  4: 0x0031 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x003F
  5: 0x0039 [0x48] [System] [7373*]:
    → "You find nothing."
  6: 0x003C [0x01] GOTO 0x007D
  7: 0x003F [0x02] IF !(ExtData[1]->WorkLocal[0] == 4*) GOTO 0x0052
  8: 0x0047 [0x03] Work_Zone[2] = 597*
  9: 0x004C [0x48] [System] [7417*]:
    → "You successfully dig up $0!"
 10: 0x004F [0x01] GOTO 0x007D
 11: 0x0052 [0x02] IF !(ExtData[1]->WorkLocal[0] == 8*) GOTO 0x0065
 12: 0x005A [0x03] Work_Zone[3] = 605*
 13: 0x005F [0x48] [System] [7372*]:
    → "Your $1 breaks!"
 14: 0x0062 [0x01] GOTO 0x007D
 15: 0x0065 [0x02] IF !(ExtData[1]->WorkLocal[0] == 12*) GOTO 0x007D
 16: 0x006D [0x03] Work_Zone[3] = 597*
 17: 0x0072 [0x03] Work_Zone[4] = 605*
 18: 0x0077 [0x48] [System] [7371*]:
    → "You find $1, but your $2 breaks in the process."
 19: 0x007A [0x01] GOTO 0x007D

SUBROUTINE_007D:
 20: 0x007D [0x21] END_EVENT
 21: 0x007E [0x00] END_REQSTACK()
```

### Event 57

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x007F   |
| Data Size    | 18 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0070:                                               42                 B
0080: 6E F0 FF FF 7F 02 80 99  F0 FF FF 7F 48 0D 80 21  n...........H..!
0090: 00                                                .               
```

#### Opcodes

```
  0: 0x007F [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0080 [0x6E] LocalPlayer uses emote 41*
  2: 0x0087 [0x99] Wait for LocalPlayer animation to complete
  3: 0x008C [0x48] [System] [7420*]:
    → "You cannot carry any more items. Your inventory is full."
  4: 0x008F [0x21] END_EVENT
  5: 0x0090 [0x00] END_REQSTACK()
```
