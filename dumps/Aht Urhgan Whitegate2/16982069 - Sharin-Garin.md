# 16982069 - Sharin-Garin

## Common Data

| Field            | Value                          |
|------------------|--------------------------------|
| Zone             | Aht Urhgan Whitegate2 (ID: 50) |
| Block Size       | 132 bytes                      |
| Total Events     | 3                              |
| References Count | 6                              |

## List of Events

| Event ID                 | Entrypoint   |   Size |   Instructions |
|--------------------------|--------------|--------|----------------|
| [65535](#event-65535)    | 0x0000       |      1 |              1 |
| [269](#event-269)        | 0x0001       |      1 |              1 |
| [65535.1](#event-655351) | 0x0002       |     75 |             11 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x001E      |          30 |
|       1 | 0x0028      |          40 |
|       2 | 0x0078      |         120 |
|       3 | 0x0000      |           0 |
|       4 | 0x003C      |          60 |
|       5 | 0x002A      |          42 |

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

### Event 269

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
| Data Size    | 75 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:       1E 30 21 03 01 1C  00 80 66 01 80 F8 FF FF    .0!.....f.....
0010: 7F F8 FF FF 7F 74 6C 6B  30 1C 02 80 66 01 80 F8  .....tlk0...f...
0020: FF FF 7F F8 FF FF 7F 74  6C 6B 31 6E 30 21 03 01  .......tlk1n0!..
0030: 03 80 99 30 21 03 01 1C  04 80 66 05 80 F8 FF FF  ...0!.....f.....
0040: 7F F8 FF FF 7F 62 69 6B  30 1C 04 80 00           .....bik0....   
```

#### Opcodes

```
  0: 0x0002 [0x1E] EventEntity looks at Bashraf (ID: 16982320/0x01032130) and starts talking
  1: 0x0007 [0x1C] WAIT(30* ticks)
  2: 0x000A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  3: 0x0019 [0x1C] WAIT(120* ticks)
  4: 0x001C [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  5: 0x002B [0x6E] Bashraf (ID: 16982320/0x01032130) uses emote 0*
  6: 0x0032 [0x99] Wait for Bashraf (ID: 16982320/0x01032130) animation to complete
  7: 0x0037 [0x1C] WAIT(60* ticks)
  8: 0x003A [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "bik0" with entities [EventEntity, EventEntity], work=42*
  9: 0x0049 [0x1C] WAIT(60* ticks)
 10: 0x004C [0x00] END_REQSTACK()
```
