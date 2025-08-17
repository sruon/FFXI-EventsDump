# 16986747 - Mythralline Wellspring

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Wajaom Woodlands (ID: 51) |
| Block Size       | 72 bytes                  |
| Total Events     | 2                         |
| References Count | 2                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [6](#event-6)         | 0x0001       |     38 |             10 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0027      |          39 |
|       1 | 0x003C      |          60 |

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

### Event 6

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 38 bytes |
| Instructions | 10       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    42 4A F0 FF FF 7F F8  FF FF 7F 6F 76 F0 FF FF   BJ........ov...
0010: 7F 6E F0 FF FF 7F 00 80  99 F0 FF FF 7F 99 F0 FF  .n..............
0020: FF 7F 1C 01 80 21 00                              .....!.         
```

#### Opcodes

```
  0: 0x0001 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0002 [0x4A] LocalPlayer looks at EventEntity
  2: 0x000B [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x000C [0x76] CHECK_ENTITY_RENDER_FLAGS: Wait until LocalPlayer Render.Flags0 and Render.Flags3 conditions are met
  4: 0x0011 [0x6E] LocalPlayer uses emote 39*
  5: 0x0018 [0x99] Wait for LocalPlayer animation to complete
  6: 0x001D [0x99] Wait for LocalPlayer animation to complete
  7: 0x0022 [0x1C] WAIT(60* ticks)
  8: 0x0025 [0x21] END_EVENT
  9: 0x0026 [0x00] END_REQSTACK()
```
