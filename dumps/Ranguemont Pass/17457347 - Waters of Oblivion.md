# 17457347 - Waters of Oblivion

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Ranguemont Pass (ID: 166) |
| Block Size       | 104 bytes                 |
| Total Events     | 3                         |
| References Count | 8                         |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [8](#event-8)            | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     39 |              9 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x000D      |          13 |
|       1 | 0xFFFF5808  |  4294924296 |
|       2 | 0xFFFF6DCA  |  4294929866 |
|       3 | 0xFFFB72A4  |  4294668964 |
|       4 | 0x3545F     |      218207 |
|       5 | 0x09AD      |        2477 |
|       6 | 0x0032      |          50 |
|       7 | 0x0001      |           1 |

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

### Event 8

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

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0002   |
| Data Size    | 39 bytes |
| Instructions | 9        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       33 01 32 00 80 03  00 00 01 80 02 00 00 02    3.2...........
0010: 80 05 28 00 37 03 80 04  80 00 00 05 80 07 00 00  ..(.7...........
0020: 06 80 1C 07 80 01 0C 00  00                       .........       
```

#### Opcodes

```
  0: 0x0002 [0x33] EventEntity->Render.Flags0 |= 0x200000 // Bit 21 (flag=0x01)
  1: 0x0004 [0x32] ExtData[1]->MainSpeed = 13* * 0.1
  2: 0x0007 [0x03] ExtData[1]->WorkLocal[0] = 4294924296*
  3: 0x000C [0x02] IF !(ExtData[1]->WorkLocal[0] > 4294929866*) GOTO 0x0028
  4: 0x0014 [0x37] UPDATE_EVENT_POSITION_AND_DIR: x=-298.332*, z=218.207*, y=ExtData[1]->WorkLocal[0], direction=217.7°*
  5: 0x001D [0x07] ExtData[1]->WorkLocal[0] += 50*
  6: 0x0022 [0x1C] WAIT(1* ticks)
  7: 0x0025 [0x01] GOTO 0x000C
  8: 0x0028 [0x00] END_REQSTACK()
```
