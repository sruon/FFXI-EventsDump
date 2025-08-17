# 17739808 - Harmodios

## Common Data

| Field            | Value                    |
|------------------|--------------------------|
| Zone             | Bastok Markets (ID: 235) |
| Block Size       | 120 bytes                |
| Total Events     | 3                        |
| References Count | 6                        |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [430](#event-430)     | 0x0001       |     52 |             12 |
| [491](#event-491)     | 0x0035       |     14 |              6 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x23F6      |        9206 |
|       1 | 0x001E      |          30 |
|       2 | 0x23FD      |        9213 |
|       3 | 0x0000      |           0 |
|       4 | 0x23FE      |        9214 |
|       5 | 0x3088      |       12424 |

## String References

- **9206**: <Player>'s badge flashes brightly.
- **9213**: What's this? Is that a Salaheem's Sentinel badge from Aht Urhgan you've got there?
- **9214**: This is quite an exquisite piece of craftsmanship. I have heard that Aht Urhgan is as technologically advanced as Bastok--a very curious place, indeed.
- **12424**: A collaboration of circus and dance, huh? Now that's something I haven't seen since my childhood, before Troupe Valeriano disbanded after that unfortunate fire...

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

### Event 430

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 52 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 48 00 80 1E F0 FF  FF 7F 1C 01 80 1D 02 80   BH.............
0010: 23 66 03 80 F8 FF FF 7F  F8 FF FF 7F 74 6C 6B 30  #f..........tlk0
0020: 1D 04 80 23 66 03 80 F8  FF FF 7F F8 FF FF 7F 74  ...#f..........t
0030: 6C 6B 31 21 00                                    lk1!.           
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x48] [System] [9206*]:
    → "<Player>'s badge flashes brightly."
  2: 0x0005 [0x1E] EventEntity looks at LocalPlayer and starts talking
  3: 0x000A [0x1C] WAIT(30* ticks)
  4: 0x000D [0x1D] PRINT_EVENT_MESSAGE(message_id=9213*)
    → "What's this? Is that a Salaheem's Sentinel badge from Aht Urhgan you've got there?"
  5: 0x0010 [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x0011 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=0*
  7: 0x0020 [0x1D] PRINT_EVENT_MESSAGE(message_id=9214*)
    → "This is quite an exquisite piece of craftsmanship. I have heard that Aht Urhgan is as technologically advanced as Bastok--a very curious place, indeed."
  8: 0x0023 [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x0024 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=0*
 10: 0x0033 [0x21] END_EVENT
 11: 0x0034 [0x00] END_REQSTACK()
```

### Event 491

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0035   |
| Data Size    | 14 bytes |
| Instructions | 6        |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030:                1E F0 FF  FF 7F 1C 01 80 1D 05 80       ...........
0040: 23 21 00                                          #!.             
```

#### Opcodes

```
  0: 0x0035 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x003A [0x1C] WAIT(30* ticks)
  2: 0x003D [0x1D] PRINT_EVENT_MESSAGE(message_id=12424*)
    → "A collaboration of circus and dance, huh? Now that's something I haven't seen since my childhood, before Troupe Valeriano disbanded after that unfortunate fire..."
  3: 0x0040 [0x23] WAIT_FOR_DIALOG_INTERACTION
  4: 0x0041 [0x21] END_EVENT
  5: 0x0042 [0x00] END_REQSTACK()
```
