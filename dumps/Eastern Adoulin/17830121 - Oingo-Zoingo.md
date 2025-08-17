# 17830121 - Oingo-Zoingo

## Common Data

| Field            | Value                     |
|------------------|---------------------------|
| Zone             | Eastern Adoulin (ID: 257) |
| Block Size       | 144 bytes                 |
| Total Events     | 3                         |
| References Count | 5                         |

## List of Events

| Event ID              | Entrypoint   |   Size |   Instructions |
|-----------------------|--------------|--------|----------------|
| [65535](#event-65535) | 0x0000       |      1 |              1 |
| [546](#event-546)     | 0x0001       |     47 |             11 |
| [47](#event-47)       | 0x0030       |     48 |             12 |

## DAT References (imed_data)

|   Index | Hex Value   |   Dec Value |
|---------|-------------|-------------|
|       0 | 0x0028      |          40 |
|       1 | 0x26E9      |        9961 |
|       2 | 0x26EA      |        9962 |
|       3 | 0x1FBB      |        8123 |
|       4 | 0x1FBC      |        8124 |

## String References

- **8123**: You came to visitaru us on behalf of the library? Wonderful organization, no doubt.
- **8124**: Perfectaru information about the Order of Gorney. I have nothing to correct. Remember, we're always interested in new business-wusiness leads. Feel free to come back if you find anything of note!
- **9961**: Behind me stands the amazing-wazing residence of the one and only Chero-Machero. I shouldn't need to tell you that he's the minister of commerce, but I like to talk, so I will.
- **9962**: To be honestaru, he's probably too busy counting his bayldy-wayld to have an audience with you now, but come by the next time you have a business proposition.

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

### Event 546

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0001   |
| Data Size    | 47 bytes |
| Instructions | 11       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0000:    1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8   .....opf.......
0010: FF FF 7F 74 6C 6B 30 1D  01 80 23 1D 02 80 23 66  ...tlk0...#...#f
0020: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x0001 [0x1E] EventEntity looks at LocalPlayer and starts talking
  1: 0x0006 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  2: 0x0007 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  3: 0x0008 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  4: 0x0017 [0x1D] PRINT_EVENT_MESSAGE(message_id=9961*)
    → "Behind me stands the amazing-wazing residence of the one and only Chero-Machero. I shouldn't need to tell you that he's the minister of commerce, but I like to talk, so I will."
  5: 0x001A [0x23] WAIT_FOR_DIALOG_INTERACTION
  6: 0x001B [0x1D] PRINT_EVENT_MESSAGE(message_id=9962*)
    → "To be honestaru, he's probably too busy counting his bayldy-wayld to have an audience with you now, but come by the next time you have a business proposition."
  7: 0x001E [0x23] WAIT_FOR_DIALOG_INTERACTION
  8: 0x001F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
  9: 0x002E [0x21] END_EVENT
 10: 0x002F [0x00] END_REQSTACK()
```

### Event 47

#### Metadata

| Field        | Value    |
|--------------|----------|
| Entrypoint   | 0x0030   |
| Data Size    | 48 bytes |
| Instructions | 12       |

```
      00 01 02 03 04 05 06 07  08 09 0A 0B 0C 0D 0E 0F
      -- -- -- -- -- -- -- --  -- -- -- -- -- -- -- --
0030: 42 1E F0 FF FF 7F 6F 70  66 00 80 F8 FF FF 7F F8  B.....opf.......
0040: FF FF 7F 74 6C 6B 30 1D  03 80 23 1D 04 80 23 66  ...tlk0...#...#f
0050: 00 80 F8 FF FF 7F F8 FF  FF 7F 74 6C 6B 31 21 00  ..........tlk1!.
```

#### Opcodes

```
  0: 0x0030 [0x42] SET_CLI_EVENT_CANCEL_DATA()
  1: 0x0031 [0x1E] EventEntity looks at LocalPlayer and starts talking
  2: 0x0036 [0x6F] WAIT_FRAME_DELAY: Yield until WaitTime reaches zero
  3: 0x0037 [0x70] WAIT_ENTITY_RENDER_FLAG: Wait while EventEntity->Render.Flags3 bit 2 is set (cancel turn if not)
  4: 0x0038 [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk0" with entities [EventEntity, EventEntity], work=40*
  5: 0x0047 [0x1D] PRINT_EVENT_MESSAGE(message_id=8123*)
    → "You came to visitaru us on behalf of the library? Wonderful organization, no doubt."
  6: 0x004A [0x23] WAIT_FOR_DIALOG_INTERACTION
  7: 0x004B [0x1D] PRINT_EVENT_MESSAGE(message_id=8124*)
    → "Perfectaru information about the Order of Gorney. I have nothing to correct. Remember, we're always interested in new business-wusiness leads. Feel free to come back if you find anything of note!"
  8: 0x004E [0x23] WAIT_FOR_DIALOG_INTERACTION
  9: 0x004F [0x66] LOAD_EXT_SCHEDULER_MAIN: Load scheduler "tlk1" with entities [EventEntity, EventEntity], work=40*
 10: 0x005E [0x21] END_EVENT
 11: 0x005F [0x00] END_REQSTACK()
```
