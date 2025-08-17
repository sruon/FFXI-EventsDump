# 17637645 - Previous Race

## Common Data

| Field            | Value             |
|------------------|-------------------|
| Zone             | GM_Home (ID: 210) |
| Block Size       | 220 bytes         |
| Total Events     | 3                 |
| References Count | 14                |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [210](#event-210)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |    134 |             14 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0002      |           2 |
|       1 | 0x0008      |           8 |
|       2 | 0x0000      |           0 |
|       3 | 0x0004      |           4 |
|       4 | 0x005F      |          95 |
|       5 | 0x0064      |         100 |
|       6 | 0x0069      |         105 |
|       7 | 0x0052      |          82 |
|       8 | 0x0057      |          87 |
|       9 | 0x005C      |          92 |
|      10 | 0x0059      |          89 |
|      11 | 0x005D      |          93 |
|      12 | 0x0061      |          97 |
|      13 | 0x0060      |          96 |

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

### Event 210

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x0001  |
| Data Size    | 1 bytes |
| Instructions | 1       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    00                                              .              
```

#### Opcodes

```
  0: 0x0001 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value     |
|--------------|-----------|
| Entrypoint   | 0x0002    |
| Data Size    | 134 bytes |
| Instructions | 13        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       03 00 00 2A 10 14  00 00 00 80 07 00 00 2B    ...*.........+
0010: 10 B6 0B 29 10 00 00 01  80 01 80 01 80 01 80 01  ...)............
0020: 80 02 80 02 80 1A 29 00  00 03 01 00 29 10 0C 01  ......).....)...
0030: 00 14 01 00 03 80 07 01  00 2C 10 9D 00 48 00 02  .........,...H..
0040: 00 01 00 B6 0F 02 00 1B  04 80 05 80 06 80 02 80  ................
0050: 04 80 05 80 06 80 02 80  04 80 05 80 06 80 02 80  ................
0060: 04 80 05 80 06 80 02 80  07 80 08 80 09 80 02 80  ................
0070: 07 80 08 80 09 80 02 80  0A 80 0B 80 0C 80 02 80  ................
0080: 09 80 0D 80 05 80 02 80                           ........        
```

#### Opcodes

```
  0: 0x0002 [0x03] ExtData[1]->WorkLocal[0] = Work_Zone[42]
  1: 0x0007 [0x14] ExtData[1]->WorkLocal[0] *= 2*
  2: 0x000C [0x07] ExtData[1]->WorkLocal[0] += Work_Zone[43]
  3: 0x0011 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Full entity look, race=Work_Zone[41], hair=ExtData[1]->WorkLocal[0], head=8*, body=8*, hands=8*, legs=8*, feet=8*, main=0*, sub=0*)
  4: 0x0025 [0x1A] CALL_SUBROUTINE(address=0x0029)
  5: 0x0028 [0x00] END_REQSTACK()

SUBROUTINE_0029:
  6: 0x0029 [0x03] ExtData[1]->WorkLocal[1] = Work_Zone[41]
  7: 0x002E [0x0C] ExtData[1]->WorkLocal[1]--
  8: 0x0031 [0x14] ExtData[1]->WorkLocal[1] *= 4*
  9: 0x0036 [0x07] ExtData[1]->WorkLocal[1] += Work_Zone[44]
 10: 0x003B [0x9D] ExtData[1]->WorkLocal[2] = 0x0048[ExtData[1]->WorkLocal[1]] // Read WORD
 11: 0x0043 [0xB6] ENTITY_APPEARANCE_HANDLER(case=Model size, value=ExtData[1]->WorkLocal[2])
 12: 0x0047 [0x1B] RETURN
```

#### Data or dead code:

```
# Data Section: 0x0048 (64 bytes)
     0x0048: 04 80 05 80 06 80 02 80 04 80 05 80 06 80 02 80
     0x0058: 04 80 05 80 06 80 02 80 04 80 05 80 06 80 02 80
     0x0068: 07 80 08 80 09 80 02 80 07 80 08 80 09 80 02 80
     0x0078: 0A 80 0B 80 0C 80 02 80 09 80 0D 80 05 80 02 80
```
