# 17138512 - Mining Point

## Common Data

| Field            | Value                        |
|------------------|------------------------------|
| Zone             | North Gustaberg [S] (ID: 88) |
| Block Size       | 184 bytes                    |
| Total Events     | 2                            |
| References Count | 10                           |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [211](#event-211)     | 0x0001       |    119 |             31 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0029      |          41 |
|       1 | 0x025D      |         605 |
|       2 | 0x0000      |           0 |
|       3 | 0x1D90      |        7568 |
|       4 | 0xFFFFFBCA  |  4294966218 |
|       5 | 0xFFFFFBC9  |  4294966217 |
|       6 | 0x1D8E      |        7566 |
|       7 | 0x1D8D      |        7565 |
|       8 | 0x1D8F      |        7567 |
|       9 | 0x1D91      |        7569 |

## String References

- **7565**: Your $7 breaks!
- **7566**: You successfully dig up $0!
- **7567**: You dig up $0, but your $7 breaks in the process.
- **7568**: You are unable to mine anything.
- **7569**: You cannot carry any more items. Your inventory is full.

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

### Event 211

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0001    |
| Data Size    | 119 bytes |
| Instructions | 31        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 6E F0 FF FF 7F 00  80 99 F0 FF FF 7F 03 09   Bn.............
0010: 10 01 80 02 04 10 02 80  00 73 00 02 03 10 02 80  .........s......
0020: 00 4B 00 02 02 10 02 80  00 31 00 48 03 80 01 48  .K.......1.H...H
0030: 00 02 02 10 04 80 00 3B  00 21 00 02 02 10 05 80  .......;.!......
0040: 00 45 00 21 00 48 06 80  01 70 00 02 02 10 02 80  .E.!.H...p......
0050: 00 59 00 48 07 80 01 70  00 02 02 10 04 80 00 63  .Y.H...p.......c
0060: 00 21 00 02 02 10 05 80  00 6D 00 21 00 48 08 80  .!.......m.!.H..
0070: 01 76 00 48 09 80 21 00                           .v.H..!.        
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x6E] LocalPlayer uses emote 41*
  2: 0x0009 [0x99] Wait for LocalPlayer animation to complete
  3: 0x000E [0x03] Work_Zone[9] = 605*
  4: 0x0013 [0x02] IF !(Work_Zone[4] == 0*) GOTO 0x0073
  5: 0x001B [0x02] IF !(Work_Zone[3] == 0*) GOTO 0x004B
  6: 0x0023 [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0031
  7: 0x002B [0x48] [System] [7568*]:
    → "You are unable to mine anything."
  8: 0x002E [0x01] GOTO 0x0048
  9: 0x0031 [0x02] IF !(Work_Zone[2] == 4294966218*) GOTO 0x003B
 10: 0x0039 [0x21] END_EVENT
 11: 0x003A [0x00] END_REQSTACK()
 12: 0x003B [0x02] IF !(Work_Zone[2] == 4294966217*) GOTO 0x0045
 13: 0x0043 [0x21] END_EVENT
 14: 0x0044 [0x00] END_REQSTACK()
 15: 0x0045 [0x48] [System] [7566*]:
    → "You successfully dig up $0!"

SUBROUTINE_0048:
 16: 0x0048 [0x01] GOTO 0x0070
 17: 0x004B [0x02] IF !(Work_Zone[2] == 0*) GOTO 0x0059
 18: 0x0053 [0x48] [System] [7565*]:
    → "Your $7 breaks!"
 19: 0x0056 [0x01] GOTO 0x0070
 20: 0x0059 [0x02] IF !(Work_Zone[2] == 4294966218*) GOTO 0x0063
 21: 0x0061 [0x21] END_EVENT
 22: 0x0062 [0x00] END_REQSTACK()
 23: 0x0063 [0x02] IF !(Work_Zone[2] == 4294966217*) GOTO 0x006D
 24: 0x006B [0x21] END_EVENT
 25: 0x006C [0x00] END_REQSTACK()
 26: 0x006D [0x48] [System] [7567*]:
    → "You dig up $0, but your $7 breaks in the process."

SUBROUTINE_0070:
 27: 0x0070 [0x01] GOTO 0x0076
 28: 0x0073 [0x48] [System] [7569*]:
    → "You cannot carry any more items. Your inventory is full."

SUBROUTINE_0076:
 29: 0x0076 [0x21] END_EVENT
 30: 0x0077 [0x00] END_REQSTACK()
```
