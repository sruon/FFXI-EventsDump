# 17412791 - Marquis Amon

## Common Data

| Field            | Value                           |
|------------------|---------------------------------|
| Zone             | Castle Zvahl Keep [S] (ID: 155) |
| Block Size       | 204 bytes                       |
| Total Events     | 5                               |
| References Count | 10                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [16](#event-16)          | 0x0001       |     12 |              4 |
| [17](#event-17)          | 0x000D       |      9 |              3 |
| [65535.1](#event-655351) | 0x0016       |     52 |             10 |
| [65535.2](#event-655352) | 0x004A       |     52 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0001      |           1 |
|       1 | 0x0000      |           0 |
|       2 | 0xFFFE96AA  |  4294874794 |
|       3 | 0xFFFFFFCE  |  4294967246 |
|       4 | 0xFFFA2E55  |  4294585941 |
|       5 | 0xFFFF34E0  |  4294915296 |
|       6 | 0x0410      |        1040 |
|       7 | 0xFFFE87D2  |  4294870994 |
|       8 | 0x0064      |         100 |
|       9 | 0x0B3C      |        2876 |

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

### Event 16

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 12 bytes |
| Instructions | 4        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    92 01 F8 FF FF 7F A5  01 C0 00 80 00            ............   
```

#### Opcodes

```
  0: 0x0001 [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0007 [0xA5] EventEntity->Flags3.BallistaTeam |= 0x08  // Set bit 3 of BallistaTeam
  2: 0x0009 [0xC0] EventEntity->Render.Flags3 |= 0x1000 // Set bit 12 (from 1*)
  3: 0x000C [0x00] END_REQSTACK()
```

### Event 17

#### Metadata

| Field        | Value   |
|--------------|---------|
| Entrypoint   | 0x000D  |
| Data Size    | 9 bytes |
| Instructions | 3       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:                                         92 01 F8               ...
0010: FF FF 7F A4 01 00                                 ......          
```

#### Opcodes

```
  0: 0x000D [0x92] EventEntity->Render.Flags3 ^= 0x01
  1: 0x0013 [0xA4] EventEntity->Flags3.unknown_3_2 = 1
  2: 0x0015 [0x00] END_REQSTACK()
```

### Event 65535.1

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0016   |
| Data Size    | 52 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0010:                   03 00  00 01 80 03 01 00 02 80        ..........
0020: 02 00 00 01 80 00 49 00  07 01 00 03 80 37 04 80  ......I......7..
0030: 01 00 05 80 06 80 02 01  00 07 80 00 43 00 03 00  ............C...
0040: 00 00 80 1C 00 80 01 20  00 00                    ....... ..      
```

#### Opcodes

```
  0: 0x0016 [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x001B [0x03] ExtData[1]->WorkLocal[1] = 4294874794*
  2: 0x0020 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x0049
  3: 0x0028 [0x07] ExtData[1]->WorkLocal[1] += 4294967246*
  4: 0x002D [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-381.355*, z=ExtData[1]->WorkLocal[1], y=-52.000*, direction=91.4°*
  5: 0x0036 [0x02] IF !(ExtData[1]->WorkLocal[1] == 4294870994*) GOTO 0x0043
  6: 0x003E [0x03] ExtData[1]->WorkLocal[0] = 1*
  7: 0x0043 [0x1C] WAIT(1* ticks)
  8: 0x0046 [0x01] GOTO 0x0020
  9: 0x0049 [0x00] END_REQSTACK()
```

### Event 65535.2

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x004A   |
| Data Size    | 52 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0040:                                03 00 00 01 80 03            ......
0050: 01 00 07 80 02 00 00 01  80 00 7D 00 07 01 00 08  ..........}.....
0060: 80 37 04 80 01 00 05 80  09 80 02 01 00 02 80 00  .7..............
0070: 77 00 03 00 00 00 80 1C  00 80 01 54 00 00        w..........T..  
```

#### Opcodes

```
  0: 0x004A [0x03] ExtData[1]->WorkLocal[0] = 0*
  1: 0x004F [0x03] ExtData[1]->WorkLocal[1] = 4294870994*
  2: 0x0054 [0x02] IF !(ExtData[1]->WorkLocal[0] == 0*) GOTO 0x007D
  3: 0x005C [0x07] ExtData[1]->WorkLocal[1] += 100*
  4: 0x0061 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-381.355*, z=ExtData[1]->WorkLocal[1], y=-52.000*, direction=252.8°*
  5: 0x006A [0x02] IF !(ExtData[1]->WorkLocal[1] == 4294874794*) GOTO 0x0077
  6: 0x0072 [0x03] ExtData[1]->WorkLocal[0] = 1*
  7: 0x0077 [0x1C] WAIT(1* ticks)
  8: 0x007A [0x01] GOTO 0x0054
  9: 0x007D [0x00] END_REQSTACK()
```
